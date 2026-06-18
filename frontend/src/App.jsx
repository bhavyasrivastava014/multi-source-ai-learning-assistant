import { BrowserRouter, Routes, Route } from "react-router-dom";

import CoursePlanner from "./pages/CoursePlanner";
import CoursePlan from "./pages/CoursePlan";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CoursePlanner />} />
        <Route path="/course-plan" element={<CoursePlan />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;