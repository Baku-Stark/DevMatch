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
        <section
            className="relative w-full h-screen bg-fixed bg-center bg-cover"
            style={{
            backgroundImage: "url('/assets/images/devmatch_landing.png')",
            }}>
            {/* Camada escura sobre a imagem */}
            <div className="absolute inset-0 bg-black/60 backdrop-blur-sm z-0" />

            {/* Conteúdo centralizado */}
            <div className="relative z-10 flex flex-col items-center justify-center h-full text-center px-6">
            <h1
                className="heading-main"
                style={{ color: 'var(--main-color)' }}>
                Welcome to DevMatch
            </h1>
            <p
                className="text-xl md:text-2xl max-w-2xl min-h-[4rem]"
                style={{ color: 'var(--main-fg-color)' }}>
                {typedText}
            </p>
            </div>
        </section>

        <SectionContainer>
            <div>
                <h1
                className="heading-main"
                style={{ color: 'var(--main-color)' }}>
                    DevMatch - Social Media
                </h1>
            </div>
        </SectionContainer>
        </main>
    );
}