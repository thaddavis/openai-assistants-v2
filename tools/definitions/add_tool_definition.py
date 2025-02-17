add_tool_definition = {
  "type": "function",
  "function": {
    "name": "add",
    "description": "This function adds 2 numbers: a & b.",
    "parameters": {
      "type": "object",
      "properties": {
        "a": {
          "type": "number",
          "description": "left operand in the addition operation",
        },
        "b": {
          "type": "number",
          "description": "right operand in the addition operation",
        },
      },
      "required": ["a", "b"],
    },
  },
}