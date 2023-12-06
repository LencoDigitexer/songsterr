// Обработка формы поиска
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const searchInput = document.querySelector('.search-input').value.trim();
    if (!searchInput) {
        alert("Please enter a valid URL");
        return;
        }
          // Проверка на домен Songsterr
  if (searchInput.indexOf("songsterr.com") === -1) {
    alert("Invalid domain. Please enter a valid Songsterr URL.");
    return;
  }
  
  // Извлечение номера песни из URL
  const songId = searchInput.split("/").pop().replace(/^(\d+)/, "$1");
  console.log(songId);
  
  // Запрос данных о песне через API Songsterr
  fetch(`https://www.songsterr.com/api/meta/${songId}/revisions`)
    .then((response) => response.json())
    .then((data) => {
      // Отображение списка ревизий песни
      const revisionsList = data.map((revision) => ({
        revisionId: revision.revisionId,
        songId: revision.songId,
        description: revision.description,
        createdAt: revision.createdAt,
        source: revision.source,
        personId: revision.personId,
        person: revision.person,
        title: revision.title,
        artist: revision.artist,
        tracksCount: revision.tracksCount,
        reports: revision.reports,
        commentsCount: revision.commentsCount,
      }));
      
      // Отображение списка ревизий в виде Listelementов
      const listElements = revisionsList.map((revision) => (`
        <li class="result">
          <h4 class="result-title">${revision.title}</h4>
          <p class="result-artist">by ${revision.artist}</p>
          <p class="result-description">${revision.description}</p>
          <a class="result-download" href="${revision.source}">Download</a>
        </li>
      `));
      
      // Отображение списка ревизий в элементеResults
      document.querySelector(".results-list").innerHTML = listElements.join("");
    })
    .catch((error) => console.error(error));
});