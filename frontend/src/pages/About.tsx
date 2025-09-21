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

        {/* ABOUT THE DEVELOPER */}
        <div className="text-center mt-12">
            
          <h2 className="text-3xl md:text-4xl font-extrabold mb-8 text-main-color neon-pulse">
            Developer
          </h2>

          <div className="max-w-3xl mx-auto bg-gray-900/70 backdrop-blur-sm rounded-2xl shadow-xl p-8 md:p-10
                          border border-gray-700">
            {/* Profile Icon */}
            <div className="flex justify-center mb-6">
              <img
                src="https://avatars.githubusercontent.com/u/103138773?v=4"
                alt="Developer Photo"
                className="w-32 h-32 rounded-full border-4 border-main-color shadow-lg object-cover"
              />
            </div>

            {/* Name */}
            <h3 className="text-2xl font-bold text-white mb-2">
              Wallace "Baku Stark"
            </h3>

            {/* Stacks */}
            <p className="text-main-color text-lg mb-4 font-medium">
              Full Stack Developer n’ Software Engineering | Pentest - White Hat Hacking | Python | Node JS | TypeScript | Java | Spring 
            </p>

            {/* Bio */}
            <p className="text-gray-300 text-base leading-relaxed mb-6 opacity-75">
              I work as a full stack developer with solid experience in Python, Node.js, TypeScript, Java, and Spring, building robust, scalable, and secure solutions. I have knowledge in penetration testing (pentest), which allows me to integrate security from the early phases of development.With a focus on delivering value and quality, I enjoy working with good coding practices, process automation, and continuous integration. I am driven by technical challenges and constant learning.
            </p>

            {/* Social Media Links */}
            <div className="flex justify-center gap-6">
              <a
                href="https://github.com/Baku-Stark"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-300 hover:text-main-color transition-colors duration-300 cursor-pointer hover:shadow-2xl hover:scale-[1.02]"
              >
                <i className="devicon-github-original text-3xl"></i>
              </a>
              <a
                href="https://www.linkedin.com/in/wallace-freitas-92a2061b6/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-300 hover:text-main-color transition-colors duration-300 cursor-pointer hover:shadow-2xl hover:scale-[1.02]"
              >
                <i className="devicon-linkedin-plain text-3xl"></i>
              </a>
              <a
                href="https://twitter.com/Walleemc2"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-300 hover:text-main-color transition-colors duration-300 cursor-pointer hover:shadow-2xl hover:scale-[1.02]"
              >
                <i className="devicon-twitter-original text-3xl"></i>
              </a>
            </div>
          </div>
        </div>

      </SectionContainer>
    </section>
  );
}