# Port Conflict Resolution Guide

When a service fails to bind (`EADDRINUSE`), identify the owning process with `portpatrol` and gracefully terminate or reassign ports.
