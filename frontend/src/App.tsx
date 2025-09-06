import SidebarWithToggle from "./components/Sidebar/SidebarWithToggle";
import AppRoutes from "./routes/AppRoutes";

function App() {
  return (
    <>
      {/* Sidebar */}
      <SidebarWithToggle/>
      <AppRoutes/>
      {/* Footer */}
    </>
  )
}

export default App