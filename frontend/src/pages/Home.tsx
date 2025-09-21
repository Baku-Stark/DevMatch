import { useTypingEffect } from '../hooks/useTypingEffect';
import SectionContainer from '../components/Containers/SectionContainer';
import { useNavigate } from 'react-router-dom';
import { ROUTES } from '../routes/routes';

export default function Home() {
    const navigate = useNavigate();

    const typedText = useTypingEffect(
        'Connect. Mentor. Grow. A platform built for developers to share knowledge and build meaningful connections.',
        60,
        true
    );

    function NavigationPages(routeChoice : string){
        switch(routeChoice){
            case "signIn":
                navigate(ROUTES.SIGN_IN);
                break;

            case "signUp":
                navigate(ROUTES.SIGN_UP);
                break;

            default:
                break;
        }
    }

    return (
        <main>
            {/* LANDING PAGE */}
            <section
                className="relative w-full h-screen bg-fixed bg-center bg-cover"
                style={{
                    backgroundImage: "url('/assets/images/devmatch_landing.png')",
                }}>

                {/* Dark layer over the image */}
                <div className="absolute inset-0 bg-black/60 backdrop-blur-sm z-0" />

                {/* Centralized content */}
                <div className="relative z-10 flex flex-col items-center justify-center h-full text-center px-6">
                    <h1
                        className="heading-main"
                        style={{ color: 'var(--main-color)' }}>
                        Welcome
                    </h1>
                    <p
                        className="text-xl md:text-2xl max-w-2xl min-h-[4rem] opacity-80"
                        style={{ color: 'var(--main-fg-color)' }}>
                        {typedText}
                    </p>

                    <button 
                        className="mt-10 px-6 py-3 rounded-xl text-lg font-semibold shadow-md transition-all duration-300 hover:scale-105 hover:shadow-lg cursor-pointer"
                        style={{ backgroundColor: 'var(--main-color)', color: 'var(--main-bg-color)' }}
                        onClick={() => NavigationPages('signIn')}>
                        Join DevMatch Now
                    </button>
                </div>
            </section>

            {/* Curved division */}
            <div className="divider-curve" />

            <SectionContainer>
                {/* ABOUT SOCIAL MEDIA */}
                <header className='mb-12'>
                    <h1 className="heading-main text-main-color">
                        DevMatch - Social Media</h1>
                    <p className="text-lg mb-8 opacity-50">
                        Our platform connects developers to share knowledge, mentor one another, and grow together.
                    </p>
                </header>

                {/* BENEFITS */}
                <div className="flex flex-wrap justify-center gap-6">
                    <article className="article-main-style">
                        <h2 className="mb-3 text-xl">Connect</h2>
                        <p>
                            Build meaningful relationships with developers worldwide
                        </p>
                    </article>
                    <article className="article-main-style">
                        <h2 className="mb-3 text-xl">Mentor</h2>
                        <p>
                            Share your expertise and grow your skills through mentorship.
                        </p>
                    </article>
                    <article className="article-main-style">
                        <h2 className="mb-3 text-xl">Grow</h2>
                        <p>
                            Access valuable resources and foster your professional development.
                        </p>
                    </article>
                </div>

                <hr className="divider-sections" />

                {/* HOW IT WORKS */}
                <section className="py-16 bg-main-bg-color text-main-fg-color text-center">
                    <h2 className="heading-main mb-10">How It Works</h2>
                    <div className="max-w-5xl mx-auto flex flex-col md:flex-row justify-around gap-8">
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-globe text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">Discover</h3>
                            <p>Find developers and mentors suited to your goals.</p>
                        </div>
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-hand-thumbs-up-fill text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">Collaborate</h3>
                            <p>Engage in meaningful conversations and collaborations.</p>
                        </div>
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-share-fill text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">Share</h3>
                            <p>Contribute knowledge and help others grow alongside you.</p>
                        </div>
                    </div>
                </section>

                <hr className="divider-sections" />

                {/* ABOUT USERS (using fictional examples) */}
                <section className="py-16 text-center">
                    <h2 className="heading-main mb-10">What Our Users Say</h2>
                    <div className="flex flex-col md:flex-row justify-center gap-6">
                        {[
                            { name: 'Alice', text: 'DevMatch helped me find my first mentor and land my first job!' },
                            { name: 'Carlos', text: 'I love sharing my knowledge here, it feels rewarding!' },
                            { name: 'Mia', text: 'Great platform to meet developers from around the globe.' },
                        ].map((testimonial, idx) => (
                            <div
                                key={idx}
                                className="p-6 bg-main-bg-color border border-main-color rounded-xl shadow-md max-w-sm"
                            >
                                <p className="italic">“{testimonial.text}”</p>
                                <h4 className="mt-4 font-bold text-main-color">— {testimonial.name}</h4>
                            </div>
                        ))}
                    </div>
                </section>

                <hr className="divider-sections" />

                {/* CALL TO ACTION */}
                <section className="py-20 text-center bg-main-color rounded-xl shadow-lg">
                    <h2 className="text-3xl md:text-4xl font-bold mb-6 text-main-bg-color">
                        Ready to start your mentorship journey?
                    </h2>
                    <button
                        className="px-8 py-3 rounded-xl text-lg font-semibold shadow-lg transition-transform transform hover:scale-110"
                        style={{
                            backgroundColor: 'var(--main-bg-color)',
                            color: 'var(--main-color)',
                        }}
                        onClick={() => NavigationPages('signUp')}
                    >
                        Get Started Now
                    </button>
                </section>
            </SectionContainer>
        </main>
    );
}