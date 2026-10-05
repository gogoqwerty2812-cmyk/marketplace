// Force the single calm light theme before first paint, and clear any stale
// saved preference (e.g. an old "dark"). Kept in its own file (not inline) so
// the Content-Security-Policy can forbid inline scripts entirely.
(function () {
  try { localStorage.setItem("mkt_theme", "light"); } catch (e) {}
  document.documentElement.setAttribute("data-theme", "light");
})();
