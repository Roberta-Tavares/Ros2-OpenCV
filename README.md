# Ros2-OpenCV
Este repositório contém um ambiente de simulação ROS 2 integrado com o Gazebo e suporte para processamento de imagens via OpenCV, empacotado em um contêiner Docker para facilitar a portabilidade.
✔️ Desenvolvido para estudos de ROS2, sensores, tópicos e visão computacional usando OpenCV.

# 📁 Estrutura do Repositório


	Ros2-OpenCV/
	│── Dockerfile
	│── workshop_assets/
	│   ├── assets/
	│   │   ├── launch/
	│   │   ├── models/
	│   │   ├── scripts/
	│   │   └── src/
	│   ├── world/
	│   ├── package.xml
	│   └── CMakeLists.txt



Utilize o github da Professora Milena Faria ate o passo 3:

	https://github.com/milenafariap/ros2_workshop

	
# 📥 1. Clone este repositório

	git clone https://github.com/Roberta-Tavares/Ros2-OpenCV.git
	cd ros2-opencv

# 🛠️ 2. Construa a imagem Docker

	docker build -t ros2_opencv .

# 🖥️ 3. Configure acesso gráfico (X11)

No terminal do host:

	xhost +local:docker

# 🧱 4. Execute o contêiner

	docker run -it --rm \
	--name ros2_opencv_container \
	-v ~/Ros2-OpenCV/workshop_assets:/root/workshop_assets \
	-e IGN_GAZEBO_RESOURCE_PATH=/root/workshop_assets/world:/root/workshop_assets/assets \
	-e GAZEBO_MODEL_PATH=/root/workshop_assets/assets/models \
	-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
	--network host \
	ros2_opencv

# 🧪 5. Compilar dentro do container
   
	cd /root/workshop_assets
	colcon build

# ▶️ 6. Rodar simulação (launch)

	source install/setup.bash
	ros2 launch explore_world gazebo_with_bridge.launch.py

# ➡️ Após isso:

📌 Uma aba se abre com o Gazebo
📌 Você usa outra aba de terminal para rodar comandos ROS dentro do container


# 🤖 Testes de Tópicos, Sensores e Movimentação

📌 Abrir o Docker em outro terminal
Consultar o nome do container:

	docker ps

Acessar o container:

	docker exec -it ros2_opencv_container bash

1️⃣ Listar tópicos ativos

	ros2 topic list -t

2️⃣ Ver mensagens do GPS

	ros2 topic echo /gps/fix

3️⃣ Ver mensagens da câmera

	ros2 topic echo /camera/image_raw
	

# 🔧Executando os Scripts com OpenCV em Outro Container


Após abrir o Gazebo e garantir que o robô está funcionando, para rodar qualquer script que utilize OpenCV, como o visao.py, siga os passos abaixo em outro container:

Reinstale o NumPy compatível com o OpenCV:

	pip install "numpy<2" --force-reinstall

Acesse a pasta onde ficam os scripts Python:

	cd /root/workshop_assets/assets/scripts

Execute o script desejado, por exemplo:

	python3 visao.py


	
	
