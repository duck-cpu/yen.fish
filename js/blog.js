// Ensure that we're using the correct function
const markdownRenderer = marked.parse; // Use `parse()` from the `marked` class
  
// Fetch posts and inject them into the grid
fetch('posts.json')
    .then(response => response.json())
    .then(posts => {
      const postsContainer = document.querySelector('.grid');
  
      posts.forEach(post => {
        const gridItem = document.createElement('div');
        gridItem.classList.add('item', 'large');
  
        // Convert Markdown content to HTML using `marked.parse()`
        const contentHTML = markdownRenderer(post.content);
  
        // Create the image tag only if the image URL exists
        const imageTag = post.image ? `<img src="${post.image}" alt="${post.title}" />` : '';
  
        gridItem.innerHTML = `
          <div class="cards">
            <div class="cardsHeader">
              <div class="cardsControls">
                <div> <i class="fa-solid fa-arrows-up-down-left-right"></i></div>
                <div> <i class="fa-solid fa-window-minimize"></i> 
                      <i class="fa-regular fa-window-restore"></i> 
                      <i class="fa-solid fa-xmark"></i>
                </div>
              </div>
            </div>
            <div class="cardsBody">
              <h2><a href="post.html?id=${post.id}">${post.title}</a></h2>
              <p><strong>Date:</strong> ${new Date(post.date).toLocaleDateString()}</p>
              ${imageTag}  <!-- Only adds the image if the URL exists -->
              <div>${contentHTML.substring(0, 200)}...</div>
              <a href="post.html?id=${post.id}">Read More</a>
            </div>
          </div>
        `;
  
        postsContainer.appendChild(gridItem);
      });
    })
    .catch(error => console.error('Error loading posts:', error));
  