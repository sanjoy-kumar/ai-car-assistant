import { useState } from "react"
import "./App.css"

import type { Car } from './types/car';
import CarForm from "./components/CarForm"
import AskAI from "./components/AskAI"
import AnswerBox from "./components/AnswerBox"

function App() {

  const [car, setCar] = useState<Car>({
    make: "",
    model: "",
    year: "",
    mileage: ""
  })

  const [answer, setAnswer] = useState("")
  const [loading, setLoading] = useState(false)

  return (
    <div className="container">

      <h1>🚗 AI Car Assistant</h1>

      <CarForm car={car} setCar={setCar} />

      <AskAI
        car={car}
        setAnswer={setAnswer}
        setLoading={setLoading}
      />

      <AnswerBox
        answer={answer}
        loading={loading}
      />

    </div>
  )
}

export default App
