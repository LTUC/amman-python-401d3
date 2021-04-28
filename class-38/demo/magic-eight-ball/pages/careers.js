import Link from 'next/link'


export default function About() {
    return (
        <Link href="/">
            <a className="flex items-center justify-center h-screen text-4xl bg-gray-200">Back to Home</a>
        </Link>
    );
}
