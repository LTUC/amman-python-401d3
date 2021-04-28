'use strict'

import Head from 'next/head'
import Link from 'next/link'

import { useState } from 'react'
import { replies } from '../data'
import Header from '../components/header'
import QuestionForm from '../components/question-form'
import EightBall from '../components/eight-ball'
import History from '../components/history'

export default function Home() {

        </div>
      </div>
    )
  }

  function ResponseTable(props){
    // console.log(props.answeredQuestionArray)
    return(
      <table className="w-1/2 mx-auto border-4 border-collapse border-gray-500">
        <thead>
          <tr>
            <th className="pl-2 border border-black">No.</th>
            <th className="pl-2 border border-black">Question</th>
            <th className="pl-2 border border-black">Response</th>
          </tr>
        </thead>
        <tbody>
          {props.answeredQuestionArray.map(item =>{
            <tr className="odd:bg-red-400" key={item.id}>
              <td className="pl-2 border border-black">{item.id}</td>
              <td className="pl-2 border border-black">{item.question}</td>
              <td className="pl-2 border border-black">{item.reply}</td>
            </tr>
          })}
        </tbody>
      </table>
    )
  }

  function Footer(props){
    return(
      <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
        <nav>
          {/* <a href="careers">Careers</a> */}
          <Link href="/careers">
            <a>Careers</a>
          </Link>
        </nav>
      </footer>
    )
  }
}
