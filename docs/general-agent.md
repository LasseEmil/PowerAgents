# Generic Agent Pattern

Some teams choose a tool-agnostic approach, storing only a small `AGENT.md` file and a sample configuration. This pattern works for emerging LLM tools that follow similar concepts—an instruction file, optional settings, and a set of shell or editor commands executed by the agent.

Use this scaffold as a starting point when experimenting with new providers or building your own wrappers around open-source models.

**Dependencies**

- Depends entirely on the agent you plug in
- Usually requires Git and a runtime such as Node or Python
