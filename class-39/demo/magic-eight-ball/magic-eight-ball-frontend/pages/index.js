import { useState } from 'react'
import LoginForm from '../components/login-form'
import MagicEightBallGame from '../components/magic-eight-ball-game'
import { getToken, fetcher } from '../services/data-fetcher'


export default function Home() {

    const [token, setToken] = useState();

    const [username, setUsername] = useState('');

    const [hooks, setHooks] = useState();

    async function loginHandler(credentials) {

        const fetchedToken = await getToken(credentials);

        setHooks(fetcher(fetchedToken));

        setUsername(credentials.username);

        setToken(fetchedToken);
    }

    function logoutHandler() {
        setToken(null);
        setUsername('');
        setHooks(null);
    }

    if (!token) return <LoginForm onSubmit={loginHandler} />

    return <MagicEightBallGame
        useAnsweredQuestions={hooks.useAnsweredQuestions}
        useReplies={hooks.useReplies}
        onLogout={logoutHandler}
        username={username}
    />
}


