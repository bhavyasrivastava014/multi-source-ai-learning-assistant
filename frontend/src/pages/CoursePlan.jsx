import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function CoursePlan() {
    const [plan, setPlan] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        const saved = localStorage.getItem("coursePlan");

        if (saved) {
            setPlan(saved);
        }
    }, []);

    const downloadJson = () => {
        const cleaned = plan
            .replace(/^```json\s*/i, "")
            .replace(/^```\s*/i, "")
            .replace(/\s*```$/i, "")
            .trim();

        const blob = new Blob([cleaned], {
            type: "application/json",
        });

        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "course_plan.json";
        a.click();

        URL.revokeObjectURL(url);
    };

    const renderCoursePlan = () => {
        try {
            const cleaned = plan
                .replace(/^```json\s*/i, "")
                .replace(/^```\s*/i, "")
                .replace(/```$/i, "")
                .trim();

            const course = JSON.parse(cleaned);

            return (
                <div
                    style={{
                        background: "#f5f5f5",
                        padding: "25px",
                        borderRadius: "10px",
                        lineHeight: "1.8",
                        textAlign: "left",
                    }}
                >
                    <h2>{course.title}</h2>

                    <p>
                        <strong>📅 Duration:</strong> {course.duration}
                    </p>

                    <p>
                        <strong>🎯 Target Audience:</strong>{" "}
                        {course.target_audience}
                    </p>

                    <h3>🎓 Learning Goals</h3>

                    <ul>
                        {course.learning_goals?.map((goal, index) => (
                            <li key={index}>{goal}</li>
                        ))}
                    </ul>

                    {course.modules?.map((module, index) => (
                        <div
                            key={index}
                            style={{
                                marginTop: "30px",
                                padding: "20px",
                                border: "1px solid #ddd",
                                borderRadius: "8px",
                                backgroundColor: "white",
                            }}
                        >
                            <h2>📚 {module.title}</h2>

                            <h3>Objectives</h3>

                            <ul>
                                {module.objectives?.map((obj, i) => (
                                    <li key={i}>{obj}</li>
                                ))}
                            </ul>

                            <h3>Lessons</h3>

                            <ul>
                                {module.lessons?.map((lesson, i) => (
                                    <li key={i}>{lesson}</li>
                                ))}
                            </ul>

                            <h3>Resources</h3>

                            <ul>
                                {module.resources?.map((resource, i) => (
                                    <li key={i}>{resource}</li>
                                ))}
                            </ul>

                            <h3>Assessment</h3>

                            <p>{module.assessment}</p>
                        </div>
                    ))}
                </div>
            );
        } catch (error) {
            return (
                <pre
                    style={{
                        background: "#f5f5f5",
                        padding: "20px",
                        overflow: "auto",
                        whiteSpace: "pre-wrap",
                        wordBreak: "break-word",
                    }}
                >
                    {plan}
                </pre>
            );
        }
    };

    return (
        <div style={{ padding: "30px" }}>
            <h1 style={{ textAlign: "center" }}>
                Generated Course Plan
            </h1>

            {renderCoursePlan()}

            <div style={{ marginTop: "30px" }}>
                <button
                    onClick={() => navigate("/")}
                    style={{
                        padding: "10px 20px",
                        backgroundColor: "#4CAF50",
                        color: "white",
                        border: "none",
                        borderRadius: "5px",
                        cursor: "pointer",
                        marginRight: "10px",
                    }}
                >
                    ← Back to Chat
                </button>

                <button
                    onClick={downloadJson}
                    style={{
                        padding: "10px 20px",
                        cursor: "pointer",
                    }}
                >
                    ⬇ Download JSON
                </button>
            </div>
        </div>
    );
}

export default CoursePlan;