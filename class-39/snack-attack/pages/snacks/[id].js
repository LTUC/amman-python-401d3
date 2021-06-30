import Layout from "../../components/Layout";
import { fetchSnack } from "../../services/snacksAPI";

const SnackDetail = ({ snack }) => (
    <Layout>
        <h2>{snack && snack.name}</h2>
        <p>{snack && snack.description}</p>
    </Layout>
)
    
export default SnackDetail;

export async function getServerSideProps(context) {
    const id = context.query.id;
    const snack = await fetchSnack(id);

    return {
        props: {
            snack,
        }
    }
}