// RELOJ WINDOWS XP
function updateClock() {
  const clockEl = document.getElementById('clock');
  const now = new Date();
  let hours = now.getHours();
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12 || 12;
  clockEl.textContent = `${hours}:${minutes} ${ampm}`;
}
setInterval(updateClock, 1000);
updateClock();

// INTERACCIÓN CON CARPETAS
document.querySelectorAll('.desktop-item').forEach(item => {
  item.addEventListener('click', () => {
    document.querySelectorAll('.desktop-item').forEach(i => i.style.background = 'transparent');
    item.style.background = '#e5f0ff';
    item.style.outline = '1px dotted #316ac5';
  });
  item.addEventListener('dblclick', () => {
    const techName = item.querySelector('.item-name').textContent;
    alert(`Windows XP Explorer:\nAbriendo documentación o detalles de: ${techName}`);
  });
});

// SIMULADOR DEL JUEGO SNAKE SOBRE EL GRAPH DE CONTRIBUCIONES GITHUB
(function initSnake() {
  const canvas = document.getElementById('snakeCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const eatenDisplay = document.getElementById('eatenCount');

  const cellSize = 10;
  const cols = Math.floor(canvas.width / cellSize);
  const rows = Math.floor(canvas.height / cellSize);

  // Generar matriz de "commits" verdes estilo GitHub
  const colors = ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'];
  const grid = [];
  for (let c = 0; c < cols; c++) {
    grid[c] = [];
    for (let r = 0; r < rows; r++) {
      // 60% probabilidad de commit
      const level = Math.random() > 0.4 ? Math.floor(Math.random() * 4) + 1 : 0;
      grid[c][r] = level;
    }
  }

  // Estado de la serpiente
  let snake = [
    { x: 5, y: 5 },
    { x: 4, y: 5 },
    { x: 3, y: 5 },
    { x: 2, y: 5 },
  ];
  let direction = { x: 1, y: 0 };
  let eatenCount = 0;

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Dibujar celdas de contribuciones
    for (let c = 0; c < cols; c++) {
      for (let r = 0; r < rows; r++) {
        ctx.fillStyle = colors[grid[c][r]];
        ctx.fillRect(c * cellSize + 1, r * cellSize + 1, cellSize - 2, cellSize - 2);
      }
    }

    // Mover serpiente de forma autónoma buscando comida o patrullando
    const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

    // Si choca contra pared o aleatoriamente, cambia de dirección
    if (
      head.x < 0 || head.x >= cols ||
      head.y < 0 || head.y >= rows ||
      Math.random() < 0.08
    ) {
      const dirs = [
        { x: 1, y: 0 },
        { x: -1, y: 0 },
        { x: 0, y: 1 },
        { x: 0, y: -1 }
      ].filter(d => !(d.x === -direction.x && d.y === -direction.y));

      // Buscar una dirección válida dentro del marco
      const validDirs = dirs.filter(d => {
        const nx = snake[0].x + d.x;
        const ny = snake[0].y + d.y;
        return nx >= 0 && nx < cols && ny >= 0 && ny < rows;
      });

      if (validDirs.length > 0) {
        direction = validDirs[Math.floor(Math.random() * validDirs.length)];
      }
    }

    const newHead = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

    // Envolver bordes por si acaso
    if (newHead.x < 0) newHead.x = cols - 1;
    if (newHead.x >= cols) newHead.x = 0;
    if (newHead.y < 0) newHead.y = rows - 1;
    if (newHead.y >= rows) newHead.y = 0;

    snake.unshift(newHead);

    // Si la celda tenía commit verde (> 0), la serpiente "se lo come"
    if (grid[newHead.x][newHead.y] > 0) {
      grid[newHead.x][newHead.y] = 0; // Celda comida vuelve a vacía
      eatenCount++;
      if (eatenDisplay) eatenDisplay.textContent = eatenCount;
    } else {
      snake.pop();
    }

    // Dibujar serpiente retro
    snake.forEach((segment, index) => {
      ctx.fillStyle = index === 0 ? '#1b4332' : '#2d6a4f';
      ctx.fillRect(segment.x * cellSize, segment.y * cellSize, cellSize, cellSize);

      // Ojos de la serpiente
      if (index === 0) {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(segment.x * cellSize + 2, segment.y * cellSize + 2, 2, 2);
      }
    });
  }

  setInterval(draw, 120);
})();
