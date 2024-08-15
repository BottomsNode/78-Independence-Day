// JavaScript to start audio on user interaction
document.addEventListener('DOMContentLoaded', () => {
    const audio = document.getElementById('background-audio');
    const playButton = document.getElementById('play-button');

    audio.volume = 1.0;

    playButton.addEventListener('click', () => {
        if (audio.paused) {
            audio.play().catch(error => {
                console.log('Audio play failed:', error);
            });
            playButton.textContent = 'Pause Anthem';
        } else {
            audio.pause();
            playButton.textContent = 'Play Anthem';
        }
    });
});
