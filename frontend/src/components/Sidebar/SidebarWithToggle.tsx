import { useEffect, useState } from "react";
import { Home, Settings, LogOut, Menu, X, LogIn } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { ROUTES } from "../../routes/routes";

export default function SidebarWithToggle() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [activeItem, setActiveItem] = useState("Dashboard");
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const toggleSidebar = () => setSidebarOpen(!sidebarOpen);

  const navItems = [
    { label: "Home", icon: Home, href: ROUTES.HOME },
    { label: "About", icon: Settings, href: ROUTES.ABOUT },
  ];

  // 🔹 Disable the body scroll when the sidebar is open
  useEffect(() => {
    if (sidebarOpen) {
      document.body.style.overflow = "hidden"; // disable scroll
    } else {
      document.body.style.overflow = ""; // reactive scroll
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [sidebarOpen]);

  const handleAuthClick = async () => {
    if (user) {
      await logout();
      navigate(ROUTES.SIGN_IN);
    } else {
      navigate(ROUTES.SIGN_UP);
    }
    setSidebarOpen(false);
  };

  return (
    <>
      {/* Botão hambúrguer */}
      {!sidebarOpen && (
        <button
          onClick={toggleSidebar}
          className="fixed top-4 left-4 z-20 p-2 rounded-md bg-main-color text-main-fg-color shadow-md hover:bg-main-fg-color hover:text-main-color transition"
          aria-label="Toggle sidebar"
        >
          <Menu className="w-6 h-6" />
        </button>
      )}

      {/* Sidebar */}
      <aside
        className={`
          fixed top-0 left-0 h-full w-64 bg-main-bg-color text-main-fg-color shadow-2xl z-30
          transform transition-transform duration-300
          ${sidebarOpen ? "translate-x-0" : "-translate-x-full"}
        `}
      >
        {/* Header da Sidebar */}
        <div className="flex justify-between items-center p-6 border-b border-gray-800">
          <img
            src="/assets/images/devmatch_icon.png"
            alt="DevMatch Icon"
            style={{ width: "25px", height: "25px" }}
          />
          <h2 className="text-2xl font-bold text-main-color tracking-wide">
            DevMatch
          </h2>
          <button
            onClick={toggleSidebar}
            className="p-2 rounded-md hover:bg-gray-800 transition"
          >
            <X className="w-6 h-6 text-main-fg-color" />
          </button>
        </div>

        {/* Navegação */}
        <nav className="flex flex-col gap-3 p-6">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeItem === item.label;

            return (
              <Link
                key={item.label}
                to={item.href}
                onClick={() => {
                  setActiveItem(item.label);
                  setSidebarOpen(false);
                }}
                className={`
                  flex items-center gap-4 px-4 py-3 rounded-lg text-lg font-medium transition-all duration-300
                  ${
                    isActive
                      ? "bg-main-color text-white shadow-lg"
                      : "hover:bg-gray-800 hover:text-main-color"
                  }
                `}
              >
                <Icon
                  className={`w-6 h-6 ${
                    isActive ? "text-white" : "text-main-color"
                  }`}
                />
                {item.label}
              </Link>
            );
          })}
        </nav>

        {/* Divider */}
        <div className="border-t border-gray-800 my-4 mx-6" />

        {/* Botão de Logout ou Sign In */}
        <div className="p-6">
          <button
            onClick={handleAuthClick}
            className={`flex items-center gap-4 px-4 py-3 rounded-lg text-lg font-medium transition-all duration-300 w-full
              ${
                user
                  ? "text-red-500 hover:bg-red-500 hover:text-white"
                  : "text-green-500 hover:bg-green-500 hover:text-white"
              }
            `}
          >
            {user ? (
              <>
                <LogOut className="w-6 h-6" />
                Logout
              </>
            ) : (
              <>
                <LogIn className="w-6 h-6" />
                Sign In
              </>
            )}
          </button>
        </div>
      </aside>

      {/* Overlay mais escuro com opacity-75 */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black opacity-75 z-20 transition-opacity duration-300"
          onClick={toggleSidebar}
        />
      )}
    </>
  );
}