# Drought Risk Insurance Monitor

An end-to-end climate risk analytics platform and monitoring dashboard designed for index-based (parametric) drought insurance. The system automates the lifecycle of weather-indexed underwriting by ingesting environmental telemetry, modeling drought severity, and evaluating index triggers for fast, objective insurance settlements.

## Overview

Traditional agricultural insurance often suffers from slow claim validation and high administrative loss-adjustment costs. **Drought Risk Insurance Monitor** provides an objective, data-driven alternative by linking claim verification directly to verifiable environmental indices (e.g., precipitation deficits, soil moisture anomalies, or vegetation health indices).

## Key Features

- **Automated Data Ingestion (`fetch_data.py`):** Automatically retrieves climate indicators and historical drought observations across designated coverage regions.
- **Reproducible Data Pipeline (`drought_processed.csv`):** Cleans, standardizes, and normalizes raw telemetry into structured feature sets ready for statistical analysis and modeling.
- **Parametric Risk Modeling (`model.py`):** Evaluates risk exposure, classifies severity tiers, and identifies predefined parametric trigger thresholds required for policy settlements.
- **Interactive Monitoring Dashboard (`app.py`):** Offers a centralized interface for monitoring regional drought exposure, viewing payout triggers, and reviewing predictive risk metrics in real time.

## Project Structure

```text
├── app.py                  # Web dashboard for monitoring risk and triggers
├── fetch_data.py           # Ingestion script for climate and environmental data
├── model.py                # Machine learning / parametric risk model
├── drought_data.csv        # Raw collected environmental dataset
└── drought_processed.csv   # Normalized and preprocessed feature dataset
