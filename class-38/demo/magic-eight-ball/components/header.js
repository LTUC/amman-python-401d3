import Link from 'next/link'

export default function Header(props) {
    return (
        <header className="flex justify-between w-full px-8 py-4 text-center text-gray-100 bg-gray-500">
            <h1 className="text-4xl ">Magic 8 Ball</h1>
            <div>

                <h2>{props.answerCount} questions answered</h2>
                <nav>
                    <Link href="/careers">
                        <a className="px-2 py-1 text-gray-800 bg-gray-100 rounded-lg">Careers</a>
                    </Link>
                </nav>
            </div>
        </header>
    )
}
