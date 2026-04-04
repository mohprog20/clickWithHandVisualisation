# React AI Chat Bot

A web-based AI chat application that allows users to send messages and receive real-time responses from an AI model.
The interface mimics modern chat applications, with messages displayed dynamically and aligned based on sender type.

This project was built to explore frontend architecture in React, component communication, and integrating AI APIs into a user-facing application.

---

## Features

* Real-time chat interface
* Dynamic message rendering
* User vs AI message alignment (right/left)
* Fixed input bar for smooth UX
* Integration with AI model (Gemini API)
* Error handling for API failures
* Responsive layout with constrained width

---

## Technologies Used

* React – component-based UI
* JavaScript (ES6+) – application logic
* CSS – layout and styling
* Vite – development environment
* Google Gemini API – AI-generated responses

---

## How It Works

1. The user types a message in the input field.
2. The message is sent to the main application state.
3. The UI immediately renders the user message.
4. A request is sent to the AI model.
5. The AI response is received asynchronously.
6. The response is added to the message list and displayed on the opposite side.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mohprog20/react-AIChatBot.git
cd react-AIChatBot
```

Install dependencies:

```bash
npm install
```

---

## Environment Setup

Create a `.env` file in the root directory and add your API key:

```env
VITE_API=your_api_key_here
```

---

## Running the Project

Start the development server:

```bash
npm run dev
```

Then open the provided local URL in your browser.

---

## Project Structure

```bash
src/
 ├── App.jsx          # Main logic and state management
 ├── ChatInput.jsx    # Input component for sending messages
 ├── Messages.jsx     # Displays message list
 ├── index.css        # Styling
```



---
