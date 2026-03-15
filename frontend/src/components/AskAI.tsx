import { useState } from "react"
import API from "../api/api"
import type { Car } from '../types/car';

interface Props {
  car: Car
  setAnswer: (text: string) => void
  setLoading: (loading: boolean) => void
}

function AskAI({ car, setAnswer, setLoading }: Props) {

  const [question, setQuestion] = useState("")
  // 1. Initialize local loading state
  const [loading, setLocalLoading] = useState(false)

  const askAI = async () => {

    if (!question) return

    // 2. Set loading to true
    setLocalLoading(true)
    if (setLoading) setLoading(true)
    setAnswer("")

    try {

      const res = await API.post("/ask", {
        question,
        make: car.make,
        model: car.model,
        year: car.year,
        mileage: car.mileage
      })

      setAnswer(res.data.answer)

    } catch {

      setAnswer("Something went wrong")

    } finally {
      // 3. Set loading to false
      setLocalLoading(false)
      if (setLoading) setLoading(false)

    }

  }

  return (
    <>
      <h3>Ask a Question</h3>

      <input
        className="question-input"
        placeholder="Ask about your car..."
        onChange={(e) => setQuestion(e.target.value)}
      />


      <button onClick={askAI} disabled={loading}>
        {loading ? "Thinking..." : "Ask AI"}
      </button>
      
    </>
  )
}

export default AskAI
