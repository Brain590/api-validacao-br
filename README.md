# 🇧🇷 Brazilian Data Validation API
### *High-performance validation for CPF, CNPJ, and CEP*

A robust, lightweight API built with **FastAPI**, designed for seamless integration and deployment. Perfect for e-commerce, user registration systems, and financial applications requiring Brazilian document validation.

---

## 🚀 Features
- **CPF Validation:** Structural and mathematical verification of Individual Taxpayer Registry numbers.
- **CNPJ Validation:** Structural verification of Legal Entity Taxpayer Registry numbers.
- **CEP Lookup:** Address retrieval powered by the reliable ViaCEP public service.
- **Data Generation:** Generate valid (syntactic) CPF and CNPJ strings for development and testing.
- **RapidAPI Ready:** Ready-to-use authentication via headers.
- **MCP Integration:** Can be used as a set of tools for AI Agents via the Model Context Protocol.

---

## 🛠️ MCP Integration

To use this API with an AI Agent compatible with MCP (like Claude Desktop), add the following to your `mcp-config.json` (replacing the placeholders with your actual RapidAPI details):

```json
{
  "mcpServers": {
    "Brazil Data Validator API": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.rapidapi.com",
        "--header",
        "x-api-host: brazil-data-validator-api.p.rapidapi.com",
        "--header",
        "x-api-key: YOUR_RAPIDAPI_KEY_HERE"
      ]
    }
  }
}
```

> [!IMPORTANT]
> - Replace `YOUR_RAPIDAPI_KEY_HERE` with your personal key obtained from the [RapidAPI Dashboard](https://rapidapi.com/hub).
> - Ensure the `x-api-host` matches your specific deployment host on RapidAPI.

---

## ⚡ Deployment
This API is ready for deployment on platforms like **Heroku**, **Render**, or **Vercel**.

**Local Execution:**
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📄 Terms of Use
Validation is strictly syntactic (mathematical). It does not confirm the existence or active status of documents in government registries. For more details, see [TERMS_OF_USE.md](./TERMS_OF_USE.md).
