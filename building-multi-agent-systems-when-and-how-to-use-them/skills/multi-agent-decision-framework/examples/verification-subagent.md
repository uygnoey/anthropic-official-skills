# Example: Verification subagent loop

This pattern uses a separate verifier agent to validate implementation with explicit criteria.

```python
# Sketch based on the blog post
from anthropic import Anthropic

client = Anthropic()

class CodingAgent:
    def implement_feature(self, requirements: str) -> dict:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"Implement: {requirements}"}],
            tools=[read_file, write_file, list_directory],
        )
        return {"code": response.content, "files_changed": extract_files(response)}

class VerificationAgent:
    def verify_implementation(self, requirements: str, files_changed: list) -> dict:
        prompt = f"""\
Requirements: {requirements}
Files changed: {files_changed}

Run the test suite and verify:
1. All existing tests pass
2. New functionality works as specified
3. No obvious errors or security issues

You MUST run the complete test suite before marking as passed.
Do not mark as passing after only running a few tests.
Run: pytest --verbose
Only mark as PASSED if ALL tests pass with no failures.
"""
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
            tools=[run_tests, execute_code, read_file],
        )
        return {"passed": extract_pass_fail(response), "issues": extract_issues(response)}

def implement_with_verification(requirements: str, max_attempts: int = 3):
    for attempt in range(max_attempts):
        result = CodingAgent().implement_feature(requirements)
        verification = VerificationAgent().verify_implementation(requirements, result["files_changed"])
        if verification["passed"]:
            return result
        requirements += f"\n\nPrevious attempt failed: {verification['issues']}"
    raise Exception(f"Failed verification after {max_attempts} attempts")
```
