import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Image from 'next/image'
import { useState, useEffect } from 'react'

// TIP: trim down to just 6 items to more easily test "no repeat" rule
const productNames = ['bag', 'banana', 'bathroom', 'boots', 'breakfast', 'bubblegum', 'chair', 'cthulhu', 'dog-duck', 'dragon', 'pen', 'pet-sweep', 'scissors', 'shark', 'sweep', 'tauntaun', 'unicorn', 'usb', 'water-can', 'wine-glass'];

const allProducts = productNames.map(productName => {
    return { name: productName, votes: 0, views: 0 }
});


export default function Home() {

    const [currentProducts, setCurrentProducts] = useState([]);

    useEffect(() => {
        selectCurrentProducts();
    }, []); // the array argument prevents running every render

    function selectCurrentProducts() {

        const shuffled = [...allProducts];

        shuffle(shuffled);

        const safeProducts = [];

        for (let product of shuffled) {

            if (currentProducts.includes(product)) {
                continue;
            }

            safeProducts.push(product);

            product.views += 1;

            if (safeProducts.length == 3) {
                break;
            }
        }

        setCurrentProducts(safeProducts);
    }

    function clickHandler(product) {

        product.votes += 1;

        selectCurrentProducts();
    }

    return (
        <div className={styles.container}>
            <Head>
                <title>Bus Mall</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className={styles.main}>

                <section className={styles.images}>

                    {currentProducts.map(product => (
                        < Image
                            src={`/images/${product.name}.jpg`}
                            height={300}
                            width={300}
                            alt={product.name}
                            onClick={() => clickHandler(product)}
                            key={product.name}
                        />
                    ))}

                </section>

                <section className={styles.stats}>
                    {currentProducts.map(product => (
                        <p key={product.name}>{product.name}:{product.votes}/{product.views}</p>
                    ))}
                </section>
            </main>
        </div>
    )
}

/*
https://medium.com/@nitinpatel_20236/how-to-shuffle-correctly-shuffle-an-array-in-javascript-15ea3f84bfb
*/
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * i)
        const temp = array[i]
        array[i] = array[j]
        array[j] = temp
    }
}

/*

// alternate method to initialize allProducts array

  const [allProducts, setAllProducts] = useState([])

    useEffect(() => {
        const newProducts = allProductNames.map(productName => {
            return { name: productName, votes: 0, views: 0 }
        });

        setAllProducts(newProducts);

    }, []);
*/
