module Api
  module V1
    class QuestionsController < ApplicationController
      def create
        store_id = params[:store_id]
        question = params[:question]

        if store_id.blank? || question.blank?
          render json: { error: "Invalid input" }, status: 400
          return
        end

        ai_response = PythonAiClient.ask(store_id, question)
        render json: ai_response
      end
    end
  end
end
