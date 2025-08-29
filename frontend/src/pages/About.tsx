import { useDocumentTitle } from '../hooks/useDocumentTitle';

export default function About() {
  useDocumentTitle('About');

  return (
    <section
      className="max-w-4xl mx-auto px-6 py-12 shadow-md"
      style={{
        backgroundColor: 'var(--main-bg-color)',
        color: 'var(--main-fg-color)',
      }}
    >
      <h1
        className="text-4xl font-bold mb-6"
        style={{ color: 'var(--main-color)' }}
      >
        About DevMatch
      </h1>

      <p className="text-lg mb-4">
        <strong>DevMatch</strong> is a mentorship platform designed to connect developers across experience levels, technologies, and time zones. Whether you're looking to grow as a mentee or share your expertise as a mentor, DevMatch helps you find the right match.
      </p>
      <p className="text-lg mb-4">
        The platform uses a smart matching algorithm based on tech stacks, experience level, preferred language, and availability. Once matched, users can schedule sessions, chat in real time, and exchange feedback to build reputation and trust.
      </p>
      <p className="text-lg mb-4">
        DevMatch is built with a modern stack: React + TypeScript on the frontend, Node.js or FastAPI on the backend, and PostgreSQL for robust data management. It integrates with tools like Google Calendar and supports OAuth2 login via GitHub or Google.
      </p>
      <p className="text-lg">
        Our mission is simple: <em>empower developers to learn, teach, and grow together</em>. Whether you're just starting out or you're a seasoned engineer, DevMatch is your space to connect and thrive.
      </p>
    </section>
  );
}