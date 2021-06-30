import Layout from './Layout'
import Link from 'next/link';

export default function SnacksList({ snacks }) {
    return (<ul>
        {snacks && snacks.map(snack => <SnackItem key={snack.id} snack={snack} />)}
    </ul>)
}

function SnackItem({ snack }) {
    return (<li>
        <Link href="/snacks/[id].js" as={`/snacks/${snack.id}`}>
            <a>{snack.name} - {snack.description}</a>
        </Link>
    </li>)
}