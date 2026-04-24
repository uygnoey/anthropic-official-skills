# Snippet examples (from the post)

## Manual media queries
```css
.container {
  width: 100%;
  padding: 1rem;
}

@media (min-width: 768px) {
  .container {
    padding: 2rem;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

## Tailwind utility example
```html
<div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
  <div class="card">...</div>
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

## Generated responsive example (head/style excerpt)
```html
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .header {
      position: fixed;
      top: 0;
      width: 100%;
      background: #fff;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      z-index: 100;
    }

    .feature-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
      padding: 2rem 1rem;
    }

    /* Tablet and up: 2 columns */
    @media (min-width: 768px) {
      .feature-grid {
        grid-template-columns: repeat(2, 1fr);
        padding: 3rem 2rem;
      }
    }

    /* Desktop: 3 columns */
    @media (min-width: 1024px) {
      .feature-grid {
        grid-template-columns: repeat(3, 1fr);
        padding: 4rem 2rem;
      }
    }
  </style>
</head>
```

## Grid recommendation
```css
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```
