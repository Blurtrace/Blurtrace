<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jandy José Peña Vásquez (BlurTrace) - Windows XP Profile</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Tahoma:wght@400;700&family=Franklin+Gothic+Medium&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
    }
    body, html {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: 'Tahoma', 'Segoe UI', sans-serif;
      background: #000;
    }

    /* Contenedor principal a pantalla dividida */
    .screen-wrapper {
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    /* Fondo Bliss en el lado derecho */
    .main-stage {
      flex: 1;
      display: flex;
      position: relative;
      background: #4a8df8 url('https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png') no-repeat center center;
      background-size: cover;
      overflow: hidden;
    }

    /* LADO IZQUIERDO: PANTALLA DE LOGON WINDOWS XP */
    .logon-screen {
      width: 50%;
      height: 100%;
      position: relative;
      background: radial-gradient(circle at 18% 38%, #5a91ed 0%, #1545aa 55%, #082987 100%);
      border-right: 2px solid #ff9900;
      box-shadow: 4px 0 20px rgba(0, 0, 0, 0.65);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 0;
      z-index: 10;
    }

    /* Barras azul marino superior e inferior de Windows XP */
    .xp-bar-top {
      height: 65px;
      background: linear-gradient(180deg, #092c74 0%, #00194e 100%);
      border-bottom: 2px solid #ef6900;
      box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    .xp-bar-bottom {
      height: 80px;
      background: linear-gradient(180deg, #092c74 0%, #01143c 100%);
      border-top: 2px solid #ef6900;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 30px;
      color: #fff;
    }

    .logon-center-content {
      flex: 1;
      display: flex;
      align-items: center;
      position: relative;
    }

    .logon-divider {
      position: absolute;
      top: 15%;
      bottom: 15%;
      left: 50%;
      width: 1px;
      background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(255,255,255,0.7) 30%, rgba(255,255,255,0.7) 70%, rgba(255,255,255,0));
    }

    /* Sección izquierda del logon: Brand */
    .brand-section {
      width: 50%;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      padding-right: 40px;
      text-align: right;
    }
    .win-logo-box {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      margin-bottom: 25px;
    }
    .win-flag {
      width: 60px;
      height: 60px;
      filter: drop-shadow(2px 3px 5px rgba(0,0,0,0.5));
    }
    .win-text-title {
      color: #ffffff;
      font-size: 32px;
      font-weight: bold;
      letter-spacing: -0.5px;
      display: flex;
      align-items: baseline;
      text-shadow: 1px 2px 4px rgba(0,0,0,0.7);
    }
    .win-text-title span.ms {
      font-size: 14px;
      font-style: italic;
      margin-right: 5px;
      font-weight: normal;
    }
    .win-text-title span.xp {
      color: #ff6a00;
      font-size: 26px;
      font-style: italic;
      margin-left: 2px;
    }
    .logon-instructions {
      color: #d1e2fc;
      font-size: 15px;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
      margin: 0;
    }

    /* Sección derecha del logon: Tarjeta de usuario */
    .user-section {
      width: 50%;
      padding-left: 40px;
    }
    .user-card {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      padding: 14px 22px;
      border-radius: 10px;
      background: rgba(30, 80, 185, 0.4);
      border: 2px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .user-card:hover {
      background: rgba(35, 95, 220, 0.7);
      border-color: #6da7ff;
      transform: scale(1.02);
      box-shadow: 0 0 16px rgba(109, 167, 255, 0.6);
    }
    .user-card:active {
      transform: scale(0.99);
      background: rgba(20, 65, 160, 0.9);
    }
    .user-card.active-user {
      border-color: #27c4fe;
      background: rgba(18, 70, 180, 0.85);
      box-shadow: 0 0 20px #27c4fe;
    }

    /* Marco de foto Windows XP */
    .avatar-wrapper {
      position: relative;
      width: 95px;
      height: 95px;
      border-radius: 12px;
      background: linear-gradient(135deg, #1aa3e8, #0550c6);
      padding: 4px;
      box-shadow: inset 0 0 5px rgba(0,0,0,0.5), 0 3px 6px rgba(0,0,0,0.4);
      border: 2px solid #57adff;
    }
    .avatar-inner {
      width: 100%;
      height: 100%;
      border-radius: 8px;
      overflow: hidden;
      border: 2px solid #ffaf02;
      background: #ffffff;
    }
    .avatar-inner img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .user-meta {
      color: #fff;
    }
    .user-fullname {
      font-size: 21px;
      font-weight: bold;
      color: #ffffff;
      margin: 0;
      text-shadow: 1px 2px 3px rgba(0,0,0,0.85);
    }
    .user-username {
      font-size: 15px;
      color: #e2eeff;
      margin: 3px 0;
      font-weight: bold;
    }
    .user-subtitle {
      font-size: 12px;
      color: #9eccff;
      margin: 2px 0 0 0;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    /* Botón apagar en la barra inferior */
    .turn-off-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: none;
      border: none;
      color: #fff;
      font-family: inherit;
      font-size: 14px;
      cursor: pointer;
      padding: 6px 12px;
      border-radius: 4px;
      transition: background 0.2s;
    }
    .turn-off-btn:hover {
      background: rgba(255, 255, 255, 0.15);
    }
    .power-icon {
      width: 28px;
      height: 28px;
      border-radius: 5px;
      background: linear-gradient(180deg, #e63920 0%, #a41906 100%);
      box-shadow: 0 0 4px #000;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #ff7b63;
    }
    .power-icon svg {
      width: 16px;
      height: 16px;
      stroke: #fff;
      stroke-width: 2.5;
      fill: none;
    }
    .account-tip {
      font-size: 11px;
      color: #9cbfe8;
      max-width: 320px;
      line-height: 1.35;
      text-align: right;
    }

    /* LADO DERECHO: VENTANA EXPLORADOR DE WINDOWS XP */
    .desktop-area {
      width: 50%;
      height: 100%;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 15px;
    }

    .xp-window {
      width: 95%;
      height: 94%;
      max-width: 760px;
      background: #fbfbf7;
      border-radius: 8px 8px 0 0;
      border: 3px solid #0055ea;
      box-shadow: 4px 6px 20px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    /* Barra de título Azul Luna */
    .title-bar {
      height: 32px;
      background: linear-gradient(180deg, #0058ee 0%, #3593ff 4%, #288eff 6%, #126dff 8%, #034fe4 12%, #004fe4 85%, #003cc2 90%, #002e9a 100%);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 6px 0 8px;
      color: #fff;
      font-weight: bold;
      font-size: 13px;
      text-shadow: 1px 1px 1px #001d68;
    }
    .title-bar-left {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .folder-title-icon {
      width: 16px;
      height: 16px;
    }
    .title-bar-controls {
      display: flex;
      gap: 3px;
    }
    .xp-btn {
      width: 21px;
      height: 21px;
      border-radius: 3px;
      border: 1px solid #ffffff;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.7), 1px 1px 2px rgba(0,0,0,0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #fff;
      font-weight: bold;
      font-size: 11px;
      line-height: 1;
    }
    .btn-minimize {
      background: linear-gradient(180deg, #2b70f0 0%, #1545aa 100%);
    }
    .btn-maximize {
      background: linear-gradient(180deg, #2b70f0 0%, #1545aa 100%);
    }
    .btn-close {
      background: linear-gradient(180deg, #e36a52 0%, #ba290f 100%);
    }
    .xp-btn:hover {
      filter: brightness(1.15);
    }

    /* Menú File, Edit, View... */
    .menu-bar {
      background: #ece9d8;
      border-bottom: 1px solid #d4cfbe;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 2px 6px;
      font-size: 11px;
      color: #000;
    }
    .menu-items {
      display: flex;
      gap: 12px;
    }
    .menu-item {
      cursor: pointer;
      padding: 2px 5px;
      border-radius: 2px;
    }
    .menu-item:hover {
      background: #316ac5;
      color: #fff;
    }
    .menu-win-logo {
      width: 18px;
      height: 18px;
    }

    /* Contenido interior de la ventana */
    .window-body {
      flex: 1;
      background: #ffffff;
      padding: 12px 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* Scrollbar clásico */
    .window-body::-webkit-scrollbar {
      width: 16px;
    }
    .window-body::-webkit-scrollbar-track {
      background: #f1efe2;
      border-left: 1px solid #d8d4c2;
    }
    .window-body::-webkit-scrollbar-thumb {
      background: #c2bead;
      border: 1px solid #ece9d8;
      border-radius: 2px;
    }

    /* Grilla de carpetas del stack */
    .folders-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px 8px;
    }
    .folder-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 4px;
      border-radius: 4px;
      border: 1px solid transparent;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }
    .folder-item:hover {
      background: #eef3fa;
      border-color: #b6d0f6;
    }
    .folder-item.selected {
      background: #316ac5;
      border-color: #0c3d88;
    }
    .folder-item.selected .folder-label {
      color: #fff;
      background: #0b4ab3;
      padding: 0 4px;
      border-radius: 2px;
    }

    /* Icono SVG de Carpeta Windows XP */
    .folder-graphic {
      position: relative;
      width: 58px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .folder-svg {
      width: 100%;
      height: 100%;
      filter: drop-shadow(1px 2px 2px rgba(0,0,0,0.25));
    }
    .tech-badge-overlay {
      position: absolute;
      bottom: 6px;
      font-size: 9px;
      font-weight: bold;
      color: #fff;
      padding: 1px 4px;
      border-radius: 3px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.6);
      text-transform: uppercase;
      letter-spacing: 0.3px;
      max-width: 50px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .folder-label {
      margin-top: 4px;
      font-size: 11px;
      color: #000;
      word-break: break-word;
      line-height: 1.1;
    }

    /* Fila inferior: Currently Exploring + Let's Connect */
    .window-lower-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 15px;
      margin-top: 6px;
      padding-top: 8px;
      border-top: 1px dotted #ccc;
    }

    /* Carpeta en construcción */
    .exploring-box {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 6px 8px;
      border: 1px solid #ffcc00;
      background: #fffdf2;
      border-radius: 6px;
      cursor: pointer;
    }
    .exploring-box:hover {
      background: #fff8d6;
    }
    .exploring-folder {
      position: relative;
      width: 60px;
      height: 50px;
      flex-shrink: 0;
    }
    .construction-stripes {
      position: absolute;
      inset: 12px 3px 4px 3px;
      border-radius: 2px;
      background: repeating-linear-gradient(
        -45deg,
        #f5b300,
        #f5b300 6px,
        #2b2b2b 6px,
        #2b2b2b 12px
      );
      opacity: 0.85;
      border: 1px solid #735100;
    }
    .exploring-text h4 {
      margin: 0;
      font-size: 13px;
      color: #000;
    }
    .exploring-text p {
      margin: 2px 0 0 0;
      font-size: 10px;
      color: #666;
    }

    /* Contact Links */
    .connect-box h4 {
      margin: 0 0 6px 0;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 5px;
      color: #111;
    }
    .contact-item {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
      text-decoration: none;
      color: #000;
      font-size: 11px;
      padding: 2px 4px;
      border-radius: 4px;
    }
    .contact-item:hover {
      background: #eef4fe;
      color: #0a4ebd;
    }
    .contact-badge-icon {
      width: 22px;
      height: 22px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 12px;
      font-weight: bold;
      flex-shrink: 0;
    }
    .badge-email { background: #3b82f6; }
    .badge-phone { background: #22c55e; }
    .badge-insta { background: linear-gradient(45deg, #f58529, #dd2a7b, #8134af); }

    /* Sección Snake de Contribuciones */
    .contributions-section {
      margin-top: 4px;
      background: #fbfbfb;
      border: 1px solid #d3d3d3;
      padding: 8px 10px;
      border-radius: 4px;
    }
    .contrib-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .contrib-title {
      font-size: 12px;
      font-weight: bold;
      color: #222;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .snake-status {
      font-size: 10px;
      color: #555;
    }
    #snakeCanvas {
      width: 100%;
      height: 90px;
      display: block;
      background: #ffffff;
      border: 1px solid #c9d2db;
      border-radius: 4px;
      image-rendering: pixelated;
    }

    /* BARRA DE TAREAS INFERIOR (LUNA THEME) */
    .xp-taskbar {
      height: 36px;
      background: linear-gradient(180deg, #1f2f86 0%, #3168d5 10%, #2456c3 40%, #1e45a9 80%, #17368a 100%);
      border-top: 1px solid #3c7bf6;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0;
      z-index: 100;
      box-shadow: 0 -2px 5px rgba(0,0,0,0.3);
    }
    .taskbar-left {
      display: flex;
      align-items: center;
      height: 100%;
    }
    .start-button {
      height: 100%;
      background: linear-gradient(180deg, #388e3c 0%, #43a047 15%, #2e7d32 80%, #1b5e20 100%);
      border: none;
      border-radius: 0 14px 14px 0;
      padding: 0 18px 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      box-shadow: inset 1px 1px 0 rgba(255,255,255,0.6), 2px 0 6px rgba(0,0,0,0.4);
    }
    .start-button:hover {
      filter: brightness(1.1);
    }
    .start-button:active {
      filter: brightness(0.9);
    }
    .start-logo {
      width: 20px;
      height: 20px;
      filter: drop-shadow(1px 1px 2px rgba(0,0,0,0.5));
    }
    .start-label {
      color: #ffffff;
      font-style: italic;
      font-size: 15px;
      font-weight: bold;
      letter-spacing: 0.5px;
      text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }

    .running-task {
      margin-left: 10px;
      background: linear-gradient(180deg, #3c82f0 0%, #1c52b8 100%);
      border: 1px solid #143e8c;
      padding: 2px 14px;
      border-radius: 3px;
      color: #fff;
      font-size: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
      height: 26px;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.4);
    }

    .taskbar-tray {
      background: linear-gradient(180deg, #0d9ff4 0%, #086bb9 15%, #0d5a9d 100%);
      border-left: 1px solid #13467c;
      height: 100%;
      display: flex;
      align-items: center;
      padding: 0 14px;
      gap: 10px;
      color: #ffffff;
      font-size: 11px;
      box-shadow: inset 1px 0 0 rgba(255,255,255,0.3);
    }

    /* Modal retro para clicks en carpetas */
    .retro-dialog {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: #ece9d8;
      border: 3px solid #0055ea;
      border-radius: 6px 6px 0 0;
      box-shadow: 0 8px 30px rgba(0,0,0,0.5);
      z-index: 1000;
      width: 280px;
      display: none;
    }
    .retro-dialog-title {
      background: linear-gradient(180deg, #0058ee 0%, #004fe4 100%);
      color: #fff;
      font-weight: bold;
      font-size: 12px;
      padding: 4px 8px;
      display: flex;
      justify-content: space-between;
    }
    .retro-dialog-content {
      padding: 14px;
      font-size: 12px;
      text-align: center;
      color: #000;
    }
    .retro-dialog-btn {
      background: #ece9d8;
      border: 1px solid #7f9db9;
      box-shadow: inset 1px 1px 0 #fff;
      padding: 4px 16px;
      cursor: pointer;
      font-family: inherit;
      border-radius: 3px;
      margin-top: 10px;
    }
    .retro-dialog-btn:hover {
      background: #e0dcc9;
    }

    /* Responsive */
    @media (max-width: 900px) {
      .main-stage {
        flex-direction: column;
        overflow-y: auto;
      }
      .logon-screen, .desktop-area {
        width: 100%;
        height: auto;
      }
      .logon-center-content {
        flex-direction: column;
        padding: 20px 0;
      }
      .brand-section, .user-section {
        width: 100%;
        text-align: center;
        align-items: center;
        padding: 10px;
      }
      .logon-divider {
        display: none;
      }
      .folders-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      .window-lower-row {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <div class="screen-wrapper">
    <div class="main-stage">
      
      <!-- ============================================== -->
      <!-- SECCIÓN 1: LOGON DE WINDOWS XP (LADO IZQUIERDO) -->
      <!-- ============================================== -->
      <section class="logon-screen">
        <div class="xp-bar-top"></div>

        <div class="logon-center-content">
          <!-- Mitad izquierda: Marca Windows XP -->
          <div class="brand-section">
            <div class="win-logo-box">
              <svg class="win-flag" viewBox="0 0 100 100">
                <!-- Bandera Windows 4 colores -->
                <path d="M12 18 C 30 14, 42 28, 48 26 L 48 50 C 42 51, 28 38, 12 42 Z" fill="#eb3c00"/>
                <path d="M54 26 C 66 23, 78 30, 92 24 L 92 48 C 76 53, 66 48, 54 50 Z" fill="#4fa800"/>
                <path d="M12 46 C 28 42, 42 55, 48 54 L 48 78 C 42 79, 30 66, 12 70 Z" fill="#0080ff"/>
                <path d="M54 54 C 66 52, 78 57, 92 52 L 92 76 C 78 81, 66 76, 54 78 Z" fill="#ffb900"/>
              </svg>
              <div class="win-text-title">
                <span class="ms">Microsoft</span>Windows<span class="xp">xp</span>
              </div>
            </div>
            <p class="logon-instructions">To begin, click your user name</p>
          </div>

          <div class="logon-divider"></div>

          <!-- Mitad derecha: Tarjeta de perfil interactiva -->
          <div class="user-section">
            <div class="user-card" id="userCard" title="Click para iniciar sesión">
              
              <!-- FOTO DE PERFIL / AVATAR: REEMPLAZA EL SRC AQUÍ -->
              <div class="avatar-wrapper">
                <div class="avatar-inner">
                  <img id="user-avatar" 
                       src="https://github.com/BlurTrace.png" 
                       alt="Jandy José Peña Vásquez"
                       onerror="this.src='https://placehold.co/100x100/104f9e/ffffff?text=JP';">
                </div>
              </div>

              <div class="user-meta">
                <h1 class="user-fullname">Jandy José Peña Vásquez</h1>
                <div class="user-username">(BlurTrace)</div>
                <div class="user-subtitle">
                  Junior Frontend Developer in Training 🇨🇴
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- Barra inferior del Logon -->
        <div class="xp-bar-bottom">
          <button class="turn-off-btn" id="turnOffBtn">
            <div class="power-icon">
              <svg viewBox="0 0 24 24">
                <path d="M12 3v9M6.3 6.3a8 8 0 1 0 11.4 0"/>
              </svg>
            </div>
            <span>Turn off computer</span>
          </button>
          <div class="account-tip">
            After you log on, you can add or change accounts. Just go to Control Panel and click User Accounts.
          </div>
        </div>
      </section>

      <!-- ============================================== -->
      <!-- SECCIÓN 2: ESCRITORIO Y VENTANA (LADO DERECHO) -->
      <!-- ============================================== -->
      <section class="desktop-area">
        <div class="xp-window">
          <!-- Barra de título clásica Luna -->
          <div class="title-bar">
            <div class="title-bar-left">
              <svg class="folder-title-icon" viewBox="0 0 24 24" fill="#ffcc00">
                <path d="M2 5a2 2 0 0 1 2-2h4.586a1 1 0 0 1 .707.293l1.414 1.414A1 1 0 0 0 11.414 5H20a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5z"/>
              </svg>
              <span>BlurTrace - Explorer [C:\Tech Stack]</span>
            </div>
            <div class="title-bar-controls">
              <div class="xp-btn btn-minimize" title="Minimizar">_</div>
              <div class="xp-btn btn-maximize" title="Maximizar">□</div>
              <div class="xp-btn btn-close" id="winCloseBtn" title="Cerrar">✕</div>
            </div>
          </div>

          <!-- Barra de menús -->
          <div class="menu-bar">
            <div class="menu-items">
              <span class="menu-item">File</span>
              <span class="menu-item">Edit</span>
              <span class="menu-item">View</span>
              <span class="menu-item">Favorites</span>
              <span class="menu-item">Help</span>
            </div>
            <svg class="menu-win-logo" viewBox="0 0 24 24">
              <rect x="2" y="2" width="9" height="9" fill="#e73827"/>
              <rect x="13" y="2" width="9" height="9" fill="#7ac142"/>
              <rect x="2" y="13" width="9" height="9" fill="#00a4ef"/>
              <rect x="13" y="13" width="9" height="9" fill="#ffba08"/>
            </svg>
          </div>

          <!-- Interior de la ventana -->
          <div class="window-body">

            <!-- 1. Grilla de Carpetas con Badges del Tech Stack -->
            <div class="folders-grid" id="foldersContainer">
              <!-- Se inyectan dinámicamente con JS para máxima limpieza -->
            </div>

            <!-- 2. Currently Exploring & Let's Connect -->
            <div class="window-lower-row">
              <!-- Currently Exploring (Carpeta en construcción) -->
              <div class="exploring-box" id="exploringFolder" title="Abrir proyectos en curso">
                <div class="exploring-folder">
                  <svg class="folder-svg" viewBox="0 0 80 65">
                    <path d="M4 12 L 28 12 L 36 22 L 76 22 A 4 4 0 0 1 80 26 L 80 60 A 4 4 0 0 1 76 64 L 4 64 A 4 4 0 0 1 0 60 L 0 16 A 4 4 0 0 1 4 12 Z" fill="#ffd451" stroke="#c99718" stroke-width="1.5"/>
                  </svg>
                  <div class="construction-stripes"></div>
                </div>
                <div class="exploring-text">
                  <h4>🚧 Currently exploring</h4>
                  <p>Software Architecture, REST APIs, Advanced Patterns & Cloud</p>
                </div>
              </div>

              <!-- Let's Connect con Badges -->
              <div class="connect-box">
                <h4>🚀 Let's Connect!</h4>
                
                <a class="contact-item" href="mailto:jandyjpv@gmail.com" target="_blank">
                  <div class="contact-badge-icon badge-email">✉</div>
                  <div>
                    <strong>Email</strong>: jandyjpv@gmail.com
                  </div>
                </a>

                <a class="contact-item" href="tel:+573148457565">
                  <div class="contact-badge-icon badge-phone">📞</div>
                  <div>
                    <strong>Business Number</strong>: +57 314 845 7565
                  </div>
                </a>

                <a class="contact-item" href="https://www.instagram.com/blurtrace/" target="_blank">
                  <div class="contact-badge-icon badge-insta">📸</div>
                  <div>
                    <strong>Instagram</strong>: @blurtrace
                  </div>
                </a>
              </div>
            </div>

            <!-- 3. Juego / Animación de Snake para Contribuciones -->
            <div class="contributions-section">
              <div class="contrib-header">
                <span class="contrib-title">
                  🐍 Contributions Activity (Snake Game)
                </span>
                <span class="snake-status" id="snakeStats">Score: 0 | Status: Active</span>
              </div>
              <canvas id="snakeCanvas"></canvas>
            </div>

          </div>
        </div>
      </section>

    </div>

    <!-- ============================================== -->
    <!-- SECCIÓN 3: BARRA DE TAREAS LUNA INFERIOR       -->
    <!-- ============================================== -->
    <footer class="xp-taskbar">
      <div class="taskbar-left">
        <button class="start-button" id="startBtn">
          <svg class="start-logo" viewBox="0 0 100 100">
            <path d="M12 18 C 30 14, 42 28, 48 26 L 48 50 C 42 51, 28 38, 12 42 Z" fill="#eb3c00"/>
            <path d="M54 26 C 66 23, 78 30, 92 24 L 92 48 C 76 53, 66 48, 54 50 Z" fill="#4fa800"/>
            <path d="M12 46 C 28 42, 42 55, 48 54 L 48 78 C 42 79, 30 66, 12 70 Z" fill="#0080ff"/>
            <path d="M54 54 C 66 52, 78 57, 92 52 L 92 76 C 78 81, 66 76, 54 78 Z" fill="#ffb900"/>
          </svg>
          <span class="start-label">start</span>
        </button>

        <div class="running-task">
          <span>📁 C:\Tech Stack</span>
        </div>
      </div>

      <div class="taskbar-tray">
        <span>🔊</span>
        <span>🛡️</span>
        <span id="systemClock">12:00 PM</span>
      </div>
    </footer>
  </div>

  <!-- Diálogo modal retro -->
  <div class="retro-dialog" id="retroDialog">
    <div class="retro-dialog-title">
      <span id="dialogTitle">Folder Opened</span>
      <span style="cursor:pointer;" onclick="closeModal()">✕</span>
    </div>
    <div class="retro-dialog-content">
      <p id="dialogMsg">Tech Stack folder details loaded successfully.</p>
      <button class="retro-dialog-btn" onclick="closeModal()">OK</button>
    </div>
  </div>

  <script>
    /* ==============================================================
       1. DEFINICIÓN DEL TECH STACK CON COLORES OFICIALES DE BADGES
       ============================================================== */
    const techStack = [
      { name: "HTML", badge: "HTML5", color: "#E34F26", desc: "HyperText Markup Language standard" },
      { name: "CSS", badge: "CSS3", color: "#1572B6", desc: "Modern CSS with responsive design" },
      { name: "JS", badge: "JS", color: "#F7DF1E", textColor: "#000", desc: "Modern ES6+ JavaScript" },
      { name: "React", badge: "React", color: "#61DAFB", textColor: "#000", desc: "Component-based UI development" },
      { name: "NextJs", badge: "Next.js", color: "#000000", desc: "Fullstack React Framework" },
      { name: "Docker", badge: "Docker", color: "#2496ED", desc: "Containerized environments" },
      { name: "AWS", badge: "AWS", color: "#FF9900", textColor: "#000", desc: "Cloud computing infrastructure" },
      { name: "Vite", badge: "Vite", color: "#646CFF", desc: "Next-gen frontend tooling" },
      { name: "npm", badge: "npm", color: "#CB3837", desc: "Node Package Manager ecosystems" },
      { name: "VSC", badge: "VS Code", color: "#007ACC", desc: "Primary IDE & workflow" },
      { name: "PostgreSQL", badge: "Postgres", color: "#4169E1", desc: "Relational database management" },
      { name: "Prisma", badge: "Prisma", color: "#2D3748", desc: "Next-generation ORM" },
      { name: "TypeScript", badge: "TS", color: "#3178C6", desc: "Typed JavaScript development" },
      { name: "CI/CD", badge: "CI/CD", color: "#2088FF", desc: "Continuous Integration & Deployment" },
      { name: "MySQL", badge: "MySQL", color: "#4479A1", desc: "Relational SQL database" }
    ];

    // Renderizado de las carpetas de Windows XP
    const container = document.getElementById('foldersContainer');
    techStack.forEach(item => {
      const folder = document.createElement('div');
      folder.className = 'folder-item';
      folder.title = `Double-click to view details for ${item.name}`;
      folder.innerHTML = `
        <div class="folder-graphic">
          <svg class="folder-svg" viewBox="0 0 80 65">
            <defs>
              <linearGradient id="folderBack" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#ffe680"/>
                <stop offset="100%" stop-color="#f2b41c"/>
              </linearGradient>
              <linearGradient id="folderFront" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#fff2aa"/>
                <stop offset="100%" stop-color="#f8be22"/>
              </linearGradient>
            </defs>
            <path d="M4 10 L 26 10 L 34 18 L 74 18 A 4 4 0 0 1 78 22 L 78 58 A 4 4 0 0 1 74 62 L 4 62 A 4 4 0 0 1 0 58 L 0 14 A 4 4 0 0 1 4 10 Z" fill="url(#folderBack)" stroke="#bd8a0a" stroke-width="1.2"/>
            <path d="M0 24 L 78 24 L 74 60 A 4 4 0 0 1 70 64 L 6 64 A 4 4 0 0 1 2 60 Z" fill="url(#folderFront)" stroke="#c69512" stroke-width="1"/>
          </svg>
          <span class="tech-badge-overlay" style="background:${item.color}; color:${item.textColor || '#fff'}">
            ${item.badge}
          </span>
        </div>
        <span class="folder-label">${item.name}</span>
      `;

      folder.addEventListener('click', (e) => {
        document.querySelectorAll('.folder-item').forEach(f => f.classList.remove('selected'));
        folder.classList.add('selected');
      });

      folder.addEventListener('dblclick', () => {
        openModal(`Tech Stack: ${item.name}`, `Folder: C:\\Tech Stack\\${item.name}\n\n${item.desc}`);
      });

      container.appendChild(folder);
    });

    /* ==============================================================
       2. INTERACCIÓN DEL LOGON Y DIÁLOGOS RETRO
       ============================================================== */
    const userCard = document.getElementById('userCard');
    userCard.addEventListener('click', () => {
      userCard.classList.toggle('active-user');
      const soundFeedback = () => {
        try {
          const ctx = new (window.AudioContext || window.webkitAudioContext)();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
          osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15); // A5
          gain.gain.setValueAtTime(0.1, ctx.currentTime);
          gain.gain.linearRampToValueAtTime(0, ctx.currentTime + 0.25);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.25);
        } catch(e) {}
      };
      soundFeedback();
    });

    document.getElementById('turnOffBtn').addEventListener('click', () => {
      openModal("Windows XP Security", "¿Deseas apagar el equipo? (Simulación de cierre de sesión de Jandy José Peña Vásquez).");
    });

    document.getElementById('exploringFolder').addEventListener('click', () => {
      openModal("Currently Exploring", "Proyectos y arquitecturas en desarrollo: Software Architecture, Clean Code, Microservices y REST APIs.");
    });

    document.getElementById('startBtn').addEventListener('click', () => {
      openModal("Start Menu", "Jandy José Peña Vásquez (BlurTrace)\nDesarrollador Frontend Junior en constante aprendizaje.");
    });

    document.getElementById('winCloseBtn').addEventListener('click', () => {
      openModal("Explorer.exe", "La ventana del explorador no puede cerrarse por ser parte del entorno de trabajo.");
    });

    function openModal(title, msg) {
      document.getElementById('dialogTitle').innerText = title;
      document.getElementById('dialogMsg').innerText = msg;
      document.getElementById('retroDialog').style.display = 'block';
    }

    function closeModal() {
      document.getElementById('retroDialog').style.display = 'none';
    }

    /* Reloj del sistema */
    function updateClock() {
      const now = new Date();
      let hours = now.getHours();
      const mins = String(now.getMinutes()).padStart(2, '0');
      const ampm = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12 || 12;
      document.getElementById('systemClock').innerText = `${hours}:${mins} ${ampm}`;
    }
    setInterval(updateClock, 1000);
    updateClock();

    /* ==============================================================
       3. JUEGO SNAKE SOBRE LA CUADRÍCULA DE CONTRIBUCIONES DE GITHUB
       ============================================================== */
    const canvas = document.getElementById('snakeCanvas');
    const ctx = canvas.getContext('2d');

    // Paleta oficial de cuadros de contribución de GitHub
    const gitColors = ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'];
    let gridCols = 42;
    let gridRows = 7;
    let cellSize = 12;

    function resizeCanvas() {
      canvas.width = canvas.parentElement.clientWidth - 20;
      canvas.height = 84;
      cellSize = Math.floor(canvas.height / gridRows);
      gridCols = Math.floor(canvas.width / cellSize);
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Generar fondo de contribuciones pseudoaleatorio pero coherente
    const contributionGrid = [];
    for (let r = 0; r < 20; r++) {
      contributionGrid[r] = [];
      for (let c = 0; c < 100; c++) {
        const rand = Math.random();
        contributionGrid[r][c] = rand > 0.6 ? Math.floor(Math.random() * 4) + 1 : (rand > 0.3 ? 1 : 0);
      }
    }

    // Estado del Snake
    let snake = [
      { x: 12, y: 3 },
      { x: 11, y: 3 },
      { x: 10, y: 3 },
      { x: 9, y: 3 },
      { x: 8, y: 3 },
      { x: 7, y: 3 },
      { x: 6, y: 3 }
    ];
    let direction = { x: 1, y: 0 };
    let food = { x: 22, y: 3 };
    let score = 0;

    function spawnFood() {
      food = {
        x: Math.floor(Math.random() * (gridCols - 4)) + 2,
        y: Math.floor(Math.random() * gridRows)
      };
    }

    // Bucle de juego automático y guiado
    function updateSnake() {
      const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

      // IA automática para perseguir comida y que siempre esté animada como el commit graph
      if (Math.random() < 0.25 || head.x >= gridCols - 1 || head.x <= 0 || head.y >= gridRows - 1 || head.y <= 0) {
        const dx = food.x - snake[0].x;
        const dy = food.y - snake[0].y;
        if (Math.abs(dx) > Math.abs(dy)) {
          direction = { x: dx > 0 ? 1 : -1, y: 0 };
        } else {
          direction = { x: 0, y: dy > 0 ? 1 : -1 };
        }
      }

      const newHead = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

      // Bounding box loops
      if (newHead.x < 0) newHead.x = gridCols - 1;
      if (newHead.x >= gridCols) newHead.x = 0;
      if (newHead.y < 0) newHead.y = gridRows - 1;
      if (newHead.y >= gridRows) newHead.y = 0;

      snake.unshift(newHead);

      if (newHead.x === food.x && newHead.y === food.y) {
        score += 10;
        document.getElementById('snakeStats').innerText = `Score: ${score} | Contributions Eaten: ${Math.floor(score / 10)}`;
        spawnFood();
      } else {
        snake.pop();
      }
    }

    function drawContributions() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Dibujar cuadrícula de actividad
      for (let r = 0; r < gridRows; r++) {
        for (let c = 0; c < gridCols; c++) {
          const colorLevel = contributionGrid[r][c] || 0;
          ctx.fillStyle = gitColors[colorLevel];
          ctx.fillRect(c * cellSize + 1, r * cellSize + 1, cellSize - 2, cellSize - 2);
        }
      }

      // Dibujar comida (Commit dorado)
      ctx.fillStyle = '#ffaa00';
      ctx.beginPath();
      ctx.arc(food.x * cellSize + cellSize / 2, food.y * cellSize + cellSize / 2, cellSize / 3, 0, Math.PI * 2);
      ctx.fill();

      // Dibujar la Serpiente estilo Windows XP / Snake
      snake.forEach((segment, i) => {
        if (i === 0) {
          // Cabeza con ojos
          ctx.fillStyle = '#107c10';
          ctx.fillRect(segment.x * cellSize, segment.y * cellSize, cellSize, cellSize);
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(segment.x * cellSize + 2, segment.y * cellSize + 2, 3, 3);
          ctx.fillRect(segment.x * cellSize + cellSize - 5, segment.y * cellSize + 2, 3, 3);
        } else {
          ctx.fillStyle = i % 2 === 0 ? '#1f9a27' : '#2ecc71';
          ctx.fillRect(segment.x * cellSize + 1, segment.y * cellSize + 1, cellSize - 2, cellSize - 2);
        }
      });
    }

    let lastTime = 0;
    function gameLoop(time) {
      if (time - lastTime > 110) {
        updateSnake();
        drawContributions();
        lastTime = time;
      }
      requestAnimationFrame(gameLoop);
    }
    requestAnimationFrame(gameLoop);
  </script>
</body>
</html>
