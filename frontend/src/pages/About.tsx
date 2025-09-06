import SectionContainer from '../components/Containers/SectionContainer';
import { useDocumentTitle } from '../hooks/useDocumentTitle';

export default function About() {
  useDocumentTitle('About');

  return (
    <section
      className="max-w-5xl mx-auto px-6 py-12 shadow-md rounded-2xl"
      style={{
        backgroundColor: 'var(--main-bg-color)',
        color: 'var(--main-fg-color)',
      }}
    >
      {/* Título principal */}
      <h1
        className="text-5xl font-extrabold mb-6 text-center neon-pulse"
        style={{ color: 'var(--main-color)' }}
      >
        About DevMatch
      </h1>

      {/* Subtítulo */}
      <p className="text-lg text-center mb-10 max-w-3xl mx-auto opacity-80">
        <strong>DevMatch</strong> is the platform that connects developers worldwide to
        <span className="text-main-color"> learn</span>, <span className="text-main-color">share</span>, and <span className="text-main-color">grow together</span>. Whether you're a beginner or a seasoned professional, this is your place to thrive.
      </p>

      <hr className="divider-sections" />

      <SectionContainer>
        {/* Cards about social media philosophy */}
        <div className="grid md:grid-cols-3 gap-6">
          <div className="p-6 rounded-xl shadow-lg bg-gray-900 hover:scale-105 hover:shadow-xl transition-transform">
            <h3 className="text-xl font-semibold mb-3 text-main-color">Connect</h3>
            <p>
              Build meaningful relationships with developers worldwide. Find mentors,
              mentees, and collaborators based on shared interests and goals.
            </p>
          </div>

          <div className="p-6 rounded-xl shadow-lg bg-gray-900 hover:scale-105 hover:shadow-xl transition-transform">
            <h3 className="text-xl font-semibold mb-3 text-main-color">Mentor</h3>
            <p>
              Share your knowledge, grow your influence, and gain experience while
              helping others level up their skills.
            </p>
          </div>

          <div className="p-6 rounded-xl shadow-lg bg-gray-900 hover:scale-105 hover:shadow-xl transition-transform">
            <h3 className="text-xl font-semibold mb-3 text-main-color">Grow</h3>
            <p>
              Access valuable resources, improve your skills, and unlock new
              opportunities for your professional and personal development.
            </p>
          </div>
        </div>

        <hr className="divider-sections" />

        {/* Section about tecnology */}
        <div className="text-left">
          <h2 className="text-3xl font-bold mb-4 text-main-color">Our Tech Stack</h2>
          <p className="text-lg opacity-80 mb-4">
            DevMatch is built with a modern and scalable technology stack to provide
            a fast, secure, and seamless experience:
          </p>
          <ul className="list-disc list-inside space-y-2">
            <li className="mb-5">
              <strong>Frontend:</strong>  <i className="text-3xl devicon-react-original colored"></i> — <i className="text-3xl devicon-typescript-plain colored"></i> — <i className="text-3xl devicon-tailwindcss-original colored"></i>
            </li>
            <li className="mb-5">
              <strong>Backend:</strong> <i className="text-3xl devicon-fastapi-plain colored"></i> — <i className="text-3xl devicon-python-plain colored"></i>
            </li>
            <li  className="mb-5">
              <strong>Database:</strong>  <i className="text-3xl devicon-postgresql-plain colored"></i> {'('}<i>with optimized queries and views</i>{')'}
            </li>
            <li>
              <strong>Integrations:</strong> Google Calendar, OAuth2 (GitHub & Google)
            </li>
          </ul>
        </div>

        <hr className="divider-sections" />

        {/* Section about mission (devs) */}
        <div className="text-center">
          <h2 className="text-3xl font-bold mb-4 text-main-color">Our Mission</h2>
          <p className="text-lg opacity-90 max-w-3xl mx-auto">
            At <strong>DevMatch</strong>, our mission is to empower developers of all
            levels to connect, learn, and grow together.  
            We believe that collaboration accelerates innovation and helps everyone
            achieve their full potential.
          </p>
        </div>

        <hr className="divider-sections" />
      </SectionContainer>
    </section>
  );
}