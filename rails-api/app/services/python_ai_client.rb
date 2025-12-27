class PythonAiClient
  PYTHON_BASE_URL = "http://localhost:8000"

  def self.ask(store_id, question)
    conn = Faraday.new(url: PYTHON_BASE_URL)
    response = conn.post("/ask") do |req|
      req.headers["Content-Type"] = "application/json"
      req.body = {
        store_id: store_id,
        question: question
      }.to_json
    end

    JSON.parse(response.body)
  rescue Faraday::ConnectionFailed
    { error: "Python AI service is unavailable" }
  end
end
