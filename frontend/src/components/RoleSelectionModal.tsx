import { useState } from "react";

interface RoleSelectionModalProps {
  onSelect: (role: "mentor" | "mentee") => void;
}

export function RoleSelectionModal({ onSelect }: RoleSelectionModalProps) {
  const [selectedRole, setSelectedRole] = useState<"mentor" | "mentee" | null>(null);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      <div className="bg-[#1a1a1a] p-8 rounded-2xl max-w-md w-full text-center border border-gray-800">
        <h2 className="text-2xl font-bold mb-6 text-main-color">Choose Your Role</h2>
        <p className="text-gray-300 mb-6">
          Are you joining DevMatch as a <strong>Mentor</strong> or a <strong>Mentee</strong>?
        </p>

        <div className="flex justify-center gap-6 mb-6">
          <button
            onClick={() => setSelectedRole("mentor")}
            className={`px-6 py-3 rounded-xl border transition-all duration-300 ${
              selectedRole === "mentor"
                ? "bg-main-color text-black font-bold"
                : "border-gray-700 hover:bg-gray-800"
            }`}
          >
            Mentor
          </button>

          <button
            onClick={() => setSelectedRole("mentee")}
            className={`px-6 py-3 rounded-xl border transition-all duration-300 ${
              selectedRole === "mentee"
                ? "bg-main-color text-black font-bold"
                : "border-gray-700 hover:bg-gray-800"
            }`}
          >
            Mentee
          </button>
        </div>

        <button
          disabled={!selectedRole}
          onClick={() => onSelect(selectedRole!)}
          className="bg-main-color text-black px-6 py-3 rounded-xl font-semibold hover:brightness-110 transition disabled:opacity-50"
        >
          Continue
        </button>
      </div>
    </div>
  );
}
