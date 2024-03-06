document.addEventListener('DOMContentLoaded', function() {
    console.log(typeof marked); // Should output "function" if Marked is loaded
    var markdownContainer = document.getElementById('markdown-content');

    fetch('https://raw.githubusercontent.com/ollprogram/TwitchDiscordBridge/newgendev/README.md')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch Markdown file');
            }
            return response.text();
        })
        .then(markdownContent => {
            // Convert Markdown to HTML and insert into container
            markdownContainer.innerHTML = marked(markdownContent);
        })
        .catch(error => {
            console.error(error);
            markdownContainer.innerHTML = 'Failed to load Markdown content';
        });
});