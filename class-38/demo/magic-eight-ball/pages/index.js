'use strict'

import EightBall from '../components/eight-ball'
import Head from 'next/head'
import Header from '../components/header'
import History from '../components/history'
import Link from 'next/link'
import QuestionForm from '../components/question-form'
import { replies } from '../data'
import { useState } from 'react'

export default function Home() {

  const [answeredQuestions, setAnsweredQuestions] = useState([]);

  function questionAskedHandler(question) {

      const reply = replies[Math.floor(Math.random() * replies.length)];

      const answeredQuestion = {
          id: answeredQuestions.length,
          question,
          reply,
      }

      setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
  }

  return (
      <div className="h-screen py-4 bg-gray-100">
          <Head>
              <title>Magic 8 Ball</title>
              <link rel="icon" href="/favicon.ico" />
          </Head>

          <Header answerCount={answeredQuestions.length} />

          <QuestionForm onAnswer={questionAskedHandler} />

          <EightBall answeredQuestion={answeredQuestions[answeredQuestions.length - 1]} />

          <History answeredQuestions={answeredQuestions} />

      </div>
  )
}