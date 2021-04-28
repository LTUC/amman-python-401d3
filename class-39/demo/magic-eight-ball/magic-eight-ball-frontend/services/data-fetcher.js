import axios from 'axios'
import useSWR from 'swr'

const baseUrl = 'http://127.0.0.1:8000';
const tokenUrl = baseUrl + '/api/token/';
const refreshUrl = baseUrl + '/api/token/refresh';
export const apiUrl = baseUrl + '/api/v1/answers/answered-questions/';
export const repliesUrl = baseUrl + '/api/v1/answers/';


export function fetcher(token) {
    return {
        useReplies: () => useReplies(token),
        useAnsweredQuestions: () => useAnsweredQuestions(token),
    }
}

function useReplies(token) {


    const { data, error } = useSWR([repliesUrl, token], async () => {
        const config = makeConfig(token);

        const response = await axios.get(repliesUrl, config);

        return response.data.map(item => item.text);
    });

    return {
        replies: data,
        error,
    }
}

// Data hook to wrap around SWR
function useAnsweredQuestions(token) {

    const { data, error, mutate } = useSWR([apiUrl, token], fetchWithToken);

    return {
        answeredQuestions: data,
        error: error,
        mutate: mutate,
        post: async (info) => {

            const newAnsweredQuestion = new AnsweredQuestion(info);

            newAnsweredQuestion.id = -1;

            newAnsweredQuestion.question += '...'; // Add the ... to show loading state

            const updatedAnsweredQuestions = [newAnsweredQuestion, ...data]

            // this mutate-await-mutate business allows us to optimistically update data
            // then do the real fetch
            mutate(updatedAnsweredQuestions, false);

            await postWithToken(token, info);

            mutate();
        }
    }
}


// Common practice to have a "Data Access Object" to encapsulate fetched data
class AnsweredQuestion {
    constructor(info) {
        this.id = info.id;
        this.question = info.question;
        this.reply = info.reply;
    }
}

// get a JSON Web Token from server
export async function getToken(values) {

    const response = await axios.post(tokenUrl, values);

    const refreshResponse = await axios.post(refreshUrl, { refresh: response.data.refresh });

    return refreshResponse.data.access;
}



// GET from API with authentication
async function fetchWithToken(url, token) {

    const config = makeConfig(token);

    const response = await axios.get(url, config);

    const answeredQuestions = response.data.map(info => new AnsweredQuestion(info));

    return answeredQuestions;
}


// POST to API with authentication
async function postWithToken(token, info) {

    const body = {
        id: -1, // will be overwritten once cache revalidates
        question: info.question,
        reply: info.reply,
    }

    const config = makeConfig(token);

    const response = await axios.post(apiUrl, body, config);

    return response.data;
}

async function deleteWithToken(id, token) {
    const config = makeConfig(token);

    const url = apiUrl + id + '/';

    await axios.delete(url, config);

}

// helper function to handle getting Authorization headers EXACTLY right
function makeConfig(token) {
    return {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    }
}
