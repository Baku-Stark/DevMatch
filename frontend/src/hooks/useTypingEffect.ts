import { useEffect, useState } from 'react';

export function useTypingEffect(text: string, speed: number = 50, repeat: boolean = false) {
    const [displayedText, setDisplayedText] = useState('');
    const [index, setIndex] = useState(0);

    useEffect(() => {
        if (index < text.length) {
        const timeout = setTimeout(() => {
            setDisplayedText((prev) => prev + text.charAt(index));
            setIndex((prev) => prev + 1);
        }, speed);
        return () => clearTimeout(timeout);
        } else if (repeat) {
        // Reinicia o efeito após uma pequena pausa
        const resetTimeout = setTimeout(() => {
            setDisplayedText('');
            setIndex(0);
        }, 1000); // tempo de espera antes de reiniciar
        return () => clearTimeout(resetTimeout);
        }
    }, [index, text, speed, repeat]);

    return displayedText;
}
