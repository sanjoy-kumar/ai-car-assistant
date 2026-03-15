import ReactMarkdown from "react-markdown"

interface Props {
  answer: string
  loading: boolean
}

function AnswerBox({ answer, loading }: Props) {

  if (loading) {

    return (
      <div className="loader-container">
        <div className="spinner"></div>
        <p>Consulting the digital mechanic...</p>
      </div>
    )
  }

  if (!answer) return null

  return (
    <div className="answer-box">
      <h3>AI Car Response</h3>
      <ReactMarkdown>{answer}</ReactMarkdown>
    </div>
  )
}

export default AnswerBox
