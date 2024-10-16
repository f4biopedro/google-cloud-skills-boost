SELECT
*
FROM
  ML.FORECAST(MODEL `PROJECT_ID.DATASET_ID.MODEL_NAME`,
STRUCT(
      7 AS horizon,
      0.95 AS confidence_level
)
)
