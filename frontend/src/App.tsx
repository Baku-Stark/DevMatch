import SidebarWithToggle from "./components/Containers/SidebarWithToggle";
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