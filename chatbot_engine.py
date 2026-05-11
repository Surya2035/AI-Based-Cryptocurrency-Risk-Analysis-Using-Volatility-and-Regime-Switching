def chatbot_response(question, coin, volatility, regime):

    question = question.lower()

    if "risk" in question:

        if volatility > 0.05:
            return f"{coin} currently shows HIGH market risk due to high volatility."

        elif volatility > 0.02:
            return f"{coin} has moderate volatility and medium risk."

        else:
            return f"{coin} market conditions appear stable."

    if "regime" in question:

        return f"{coin} is currently in regime state {regime}"

    return "Ask about market risk or volatility."