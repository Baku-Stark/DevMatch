import { useTypingEffect } from '../hooks/useTypingEffect';

import SectionContainer from '../components/Containers/SectionContainer';

export default function Home() {
    const typedText = useTypingEffect(
        'Connect. Mentor. Grow. A platform built for developers to share knowledge and build meaningful connections.',
        60,
        true
    );

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
                </div>

            </section>

            {/* Curved division between landing and content */}
            <div className="divider-curve" />

            <SectionContainer>
                <header className='mb-12'>
                    <h1 className="heading-main text-main-color">
                        DevMatch - Social Media</h1>
                    <p className="text-lg mb-8 opacity-50">
                        Our platform connects developers to share knowledge, mentor one another, and grow together.
                    </p>
                </header>

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

                <section className="py-16 bg-main-bg-color text-main-fg-color text-center">
                    <h2 className="heading-main mb-10">How It Works</h2>
                    <div className="max-w-5xl mx-auto flex flex-col md:flex-row justify-around gap-8">
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-globe text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">
                                Discover
                            </h3>
                            <p>
                                Find developers and mentors suited to your goals.
                            </p>
                        </div>
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-hand-thumbs-up-fill text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">
                                Sections
                            </h3>
                            <p>
                                Engage in meaningful conversations and collaborations.
                            </p>
                        </div>
                        <div className="flex flex-col items-center p-6 bg-main-color rounded-xl shadow-lg">
                            <i className="bi bi-share-fill text-5xl mb-10 neon-pulse"></i>
                            <h3 className="text-xl font-semibold mb-2">
                                Share
                            </h3>
                            <p>
                                Contribute knowledge and help others grow alongside you.
                            </p>
                        </div>
                    </div>
                </section>

                <hr className="divider-sections" />

            </SectionContainer>
        </main>
    );
}