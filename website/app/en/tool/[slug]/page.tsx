import React from 'react';
import { getAllTools, getToolBySlug } from '@/lib/yaml';
import ToolView from '@/components/ToolView';

// Generate static paths at build time
export function generateStaticParams() {
  const tools = getAllTools();
  return tools.map((tool) => ({
    slug: tool.slug,
  }));
}

// Generate dynamic metadata for SEO
export function generateMetadata({ params }: { params: { slug: string } }) {
  const tool = getToolBySlug(params.slug);
  
  if (!tool) {
    return {
      title: 'Tool Not Found - AI Landscape',
    };
  }

  return {
    title: `${tool.name} - AI Landscape`,
    description: tool.description_en || tool.description || `Detailed overview and ecosystem for ${tool.name}.`,
    keywords: [...(tool.tags || []), tool.name, 'AI', 'Tools', 'Open Source'],
  };
}

export default function ToolPageEn({ params }: { params: { slug: string } }) {
  const tool = getToolBySlug(params.slug);
  return <ToolView tool={tool} locale="en" />;
}
