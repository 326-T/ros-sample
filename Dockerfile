FROM ros:humble

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python scripts
COPY src/ /app/src/

# Make the Python scripts executable
RUN chmod +x /app/src/publisher_node.py /app/src/subscriber_node.py

# Source ROS 2 setup in the entrypoint
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && exec \"$@\"", "--"]
