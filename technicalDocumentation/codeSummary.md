Codebase Summary
Overview

E-Brain Core IA is a hybrid cognitive system inspired by the human brain. It combines real-time sensor/actuator control with a lightweight AI engine for analysis, decision-making, and memory simulation.

The structure is organized into modules that represent brain areas and processing stages (perception, processing, decision, action, and feedback), making it easier to expand or replace components.

Main Structure

The brain folder groups the different “regions” of the project: medullaOblongata, cerebellum, frontalLobe, occipitalLobe, parietalLobe, temporalLobe, and neurons, each containing specialized files.

Key Components

Medulla oblongata: initializes sensors, processor, controller, and memory manager; also checks sensor status before processing data and executing actions.

Sensors: classes for audio, vision, proximity, and temperature, generating simulated data when no hardware is connected.

Memory: LongTermMemory stores data per neuron in CSV files, while ShortTermMemory keeps them in an in-memory list.

Motor control: uses PySerial to send commands to an Arduino, with basic movement routes (“left”, “right”).

Cerebellum: includes balance and motor control modules as skeletons for future coordination logic.

Sensory lobes: occipitalLobe/vision_sensor.py and parietalLobe/touch_sensor.py provide templates for vision and touch sensors.

Neurons: each nX.py file inherits from an external Neuron (not yet included), leaving the door open to a more complex neural network.

The planning document summarizes the responsibilities of each submodule and how they are expected to interact to form a modular “brain.”

Recommendations for New Contributors

Get familiar with PySerial and hardware communication to complete integration with sensors and motors.

Normalize naming conventions and language (e.g., sensorManagement vs. gestionDeSensores) to avoid confusion.

Implement the neural_network module or replace it with an existing neural network library.

Design unit tests and debugging tools for each module as real logic is added.

Deepen knowledge of data handling (CSV, lightweight databases) and minimalist AI architectures (TinyLlama or other embedded models).