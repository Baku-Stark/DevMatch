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
                    className="text-xl md:text-2xl max-w-2xl min-h-[4rem]"
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
                        <article className="text-main-style">
                            <h2 className="mb-3 text-xl">Connect</h2>
                            <p>
                                Build meaningful relationships with developers worldwide
                            </p>
                        </article>
                        <article className="text-main-style">
                            <h2 className="mb-3 text-xl">Mentor</h2>
                            <p>
                                Share your expertise and grow your skills through mentorship.
                            </p>
                        </article>
                        <article className="text-main-style">
                            <h2 className="mb-3 text-xl">Grow</h2>
                            <p>
                                Access valuable resources and foster your professional development.
                            </p>
                        </article>
                    </div>
            </SectionContainer>
        </main>
    );
}