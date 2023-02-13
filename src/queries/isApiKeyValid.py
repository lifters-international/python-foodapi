isApiKeyValid = """
    query Query($apiKey: String!) {
        isFoodApiKeyValid(api_key: $apiKey)
    }
"""