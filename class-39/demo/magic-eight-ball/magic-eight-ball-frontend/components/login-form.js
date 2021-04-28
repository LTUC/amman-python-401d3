import { useState } from 'react'
import Head from 'next/head'

export default function LoginForm(props) {

    const initialValues = {
        username: '',
        password: '',
    }

    const [values, setValues] = useState(initialValues);

    function submitHandler(event) {
        event.preventDefault();
        props.onSubmit(values);
        setValues(initialValues)
    }

    function inputChangeHandler(event) {

        let { name, value } = event.target;

        setValues({ ...values, [name]: value });
    }

    return (
        <>
            <Head>
                <title>Log In</title>
            </Head>
            <form className="flex flex-col w-1/2 gap-4 p-8 mx-auto my-4 text-center bg-gray-200 border-2 border-gray-400 rounded-lg text-md" onSubmit={submitHandler}>
                <div className="flex flex-col ">
                    <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="username">User Name</label>
                    <input className="px-3 py-2 border text-grey-darkest" type="text" name="username" id="username" value={values.username} onChange={inputChangeHandler} placeholder="User Name" />
                </div>

                <div className="flex flex-col ">
                    <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="password">Password</label>
                    <input className="px-3 py-2 border text-grey-darkest" type="password" name="password" id="password" value={values.password} onChange={inputChangeHandler} placeholder="password" />
                </div>

                <button className="px-3 py-4 mt-8 uppercase bg-gray-500 rounded text-green hover:bg-gray-600 text-gray-50" type="submit">Sign In</button>

            </form>
        </>
    );
}
