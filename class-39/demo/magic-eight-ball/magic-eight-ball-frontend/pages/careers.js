import Link from 'next/link'


export default function About() {
    return (
        <Link href="/">
            <div className="flex flex-col items-center justify-center h-screen bg-gray-200 gap-y-8">
                <a className="text-4xl">Back to Home</a>
                <p className="text-2xl">You'll have to log in again</p>
                <p className="text-6xl">🥺</p>
                <p className="text-2xl">I wonder what it would take to fix that?</p>
            </div>
        </Link>
    );
}
