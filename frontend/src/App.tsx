import AppRoutes from "../routes/AppRoutes"
import { useDocumentTitle } from "../hooks/useDocumentTitle"

function App() {
  useDocumentTitle('Home');

  return (
    <>
      <h1>Home</h1>

      <AppRoutes/>
    </>
  )
}

export default App