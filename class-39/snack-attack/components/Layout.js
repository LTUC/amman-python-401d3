import Head from 'next/head';
import Link from 'next/link';

export default function Layout({ children }) {
    return (
        <div className="flex flex-col">
            <Head>
                <title>Snack Attack</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <main>
                <nav>
                    <ul>
                        <li><Link href="/"><a>Snack Attack</a></Link></li>
                    </ul>
                </nav>
                {children}
            </main>
        <footer>
                <p> Made with 💘 in {`\u{1F1EF}\u{1F1F4}`}</p>
        </footer>
        </div>
    )
}