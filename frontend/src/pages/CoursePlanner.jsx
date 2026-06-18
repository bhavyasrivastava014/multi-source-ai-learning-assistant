import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function CoursePlanner() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [plan, setPlan] = useState("");

  useEffect(() => {
    const savedChat = localStorage.getItem("courseChat");
    const savedPlan = localStorage.getItem("coursePlan");

    if (savedChat) {
      setChat(JSON.parse(savedChat));
    }

    if (savedPlan) {
      setPlan(savedPlan);
    }
  }, []);

  const navigate = useNavigate();

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    const updatedChat = [
      ...chat,
      { role: "user", text: userMessage },
    ];

    setChat(updatedChat);
    setMessage("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/course/chat", {
        message: userMessage,
      });

      const aiReply = res.data.response;

      const finalChat = [
        ...updatedChat,
        { role: "ai", text: aiReply },
      ];

      setChat(finalChat);
      localStorage.setItem(
        "courseChat",
        JSON.stringify(finalChat)
      );

      setPlan(aiReply);
      localStorage.setItem("coursePlan", aiReply);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      {/* Left Panel */}
      <div
        style={{
          flex: 1,
          borderRight: "1px solid #ccc",
          padding: "20px",
        }}
      >
        <h2>AI Course Planner</h2>

        <div
          style={{
            height: "75%",
            overflowY: "auto",
            border: "1px solid #ddd",
            padding: "10px",
          }}
        >
          {chat.map((msg, index) => (
            <div key={index}>
              <strong>{msg.role === "user" ? "You" : "AI"}:</strong>
              <p>{msg.text}</p>
            </div>
          ))}
        </div>

        <div style={{ marginTop: "15px" }}>
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message..."
            style={{ width: "80%", padding: "10px" }}
          />

          <button
            onClick={sendMessage}
            style={{ padding: "10px", marginLeft: "10px" }}
          >
            Send
          </button>
        </div>
        {plan && (
          <div style={{ marginTop: "20px" }}>
            <button
              onClick={() => navigate("/course-plan")}
              style={{
                padding: "10px 20px",
                backgroundColor: "#4CAF50",
                color: "white",
                border: "none",
                borderRadius: "5px",
                cursor: "pointer",
              }}
            >
              📖 View Course Plan
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default CoursePlanner;